import time
from kivy.app import App
from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    is_running = BooleanProperty(False)
    elapsed_time = NumericProperty()


    def start_clock(self):
        print("Starting Clock")

    def stop_clock(self):
        print("Stopping Clock")

    def reset_clock(self):
        print("Resetting Clock")


class StopwatchApp(App):
    pass


StopwatchApp().run()