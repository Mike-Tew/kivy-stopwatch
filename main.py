import time
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    is_running = BooleanProperty(False)
    start_time = NumericProperty()
    elapsed_time = NumericProperty()
    paused_time = NumericProperty()

    def format_time(self, time_):

        return str(int(time_))

    def update_clock(self, dt):
        self.elapsed_time = time.time() - self.start_time
        print(self.elapsed_time)
        self.ids.clock_label.text = self.format_time(self.elapsed_time)

    def start_clock(self):
        self.start_time = time.time()
        self.is_running = True
        self.ids.start_button.disabled = True
        self.ids.stop_button.disabled = False
        Clock.schedule_interval(self.update_clock, 0.1)

    def stop_clock(self):
        print("Stopping Clock")
        self.is_running = False
        self.ids.stop_button.disabled = True
        self.ids.start_button.disabled = False
        Clock.unschedule(self.update_clock)

    def reset_clock(self):
        print("Resetting Clock")
        Clock.unschedule(self.update_clock)
        self.ids.start_button.disabled = False
        self.ids.stop_button.disabled = True
        self.elapsed_time = 0
        self.paused_time = 0


class StopwatchApp(App):
    def build(self):
        stopwatch = BoxLayoutExample()
        return stopwatch


if __name__ == "__main__":
    StopwatchApp().run()
