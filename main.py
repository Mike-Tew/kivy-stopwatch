import time
from kivy.app import App
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    is_running = BooleanProperty(False)
    elapsed_time = NumericProperty()

    def on_is_running(self, instance, value):
        if value == True:
            self.ids.start_button.disabled = True
            self.ids.stop_button.disabled = False
        if value == False:
            self.ids.stop_button.disabled = True
            self.ids.start_button.disabled = False

    def start_clock(self):
        print("Starting Clock")
        print(self.elapsed_time, self.is_running)
        self.is_running = True

    def stop_clock(self):
        print("Stopping Clock")
        self.is_running = False

    def reset_clock(self):
        print("Resetting Clock")
        self.ids.start_button.disabled = False
        self.ids.stop_button.disabled = True
        self.elapsed_time = 0


class StopwatchApp(App):
    pass


StopwatchApp().run()