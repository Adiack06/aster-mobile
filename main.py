import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from old.grid import MyGrid
from kivy.properties import ObjectProperty
import asterpy
import threading

class MyGrid(Widget):
    message = ObjectProperty(None)
    messages = ObjectProperty(None)
    def __init__(self):
        super().__init__()
        self.client = asterpy.Client("cospox.com", 2345, "JingKellyfish", "", 6895244034031013013)
        self._net_thread = threading.Thread(target=self.client.run)
        self._net_thread.start()

    def send_message(self):
        self.client.get_channel_by_name("general").send(self.message.text)
        self.message.text = ""
        self.msg = self.client.get_history(self.client.get_channel_by_name("general")))


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()