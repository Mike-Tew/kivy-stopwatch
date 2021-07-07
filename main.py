from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    def start_clock(self):
        print("Starting Clock")

    def stop_clock(self):
        print("Stopping Clock")

    def reset_clock(self):
        print("Resetting Clock")


class StopwatchApp(App):
    pass


StopwatchApp().run()