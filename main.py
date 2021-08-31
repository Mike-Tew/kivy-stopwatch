from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
import time


class BoxLayoutExample(BoxLayout):
    is_running = BooleanProperty(False)
    start_time = NumericProperty()
    paused_time = NumericProperty()
    elapsed_time = NumericProperty()

    def format_time(self, ms):
        display_string = datetime.fromtimestamp(28800 + ms)
        return display_string.strftime("%H:%M:%S.%f")[:-5]

    def update_clock(self, dt):
        self.elapsed_time = time.time() - self.start_time + self.paused_time
        self.ids.clock_label.text = self.format_time(self.elapsed_time)

    def start_clock(self):
        self.start_time = time.time()
        self.is_running = True
        self.ids.start_button.disabled = True
        self.ids.pause_button.disabled = False
        Clock.schedule_interval(self.update_clock, 0.1)

    def pause_clock(self):
        self.paused_time = self.elapsed_time
        self.is_running = False
        self.ids.pause_button.disabled = True
        self.ids.start_button.disabled = False
        Clock.unschedule(self.update_clock)

    def reset_clock(self):
        Clock.unschedule(self.update_clock)
        self.ids.start_button.disabled = False
        self.ids.pause_button.disabled = True
        self.elapsed_time = 0
        self.paused_time = 0
        self.ids.clock_label.text = self.format_time(self.elapsed_time)


class StopwatchApp(App):
    def build(self):
        stopwatch = BoxLayoutExample()
        return stopwatch


if __name__ == "__main__":
    StopwatchApp().run()
