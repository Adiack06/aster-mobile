from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.properties import ObjectProperty
from kivymd.uix.list import TwoLineListItem
import asterpy
import threading

KV = '''
GridLayout:
    cols:1
       
    ScrollView:
        messages: messages
        MDList:
            id: messages
    GridLayout:
        message:message
        size_hint_y: 0.05
        cols:2
        TextInput:
            id: message
            size_hint_x: 0.86
            multinline:False
        Button:
            size_hint_x: 0.14
            on_release:app.send_message()
            
    '''


class Test(MDApp):
    message = ObjectProperty(None)
    messages = ObjectProperty(None)
    def build(self):
        return Builder.load_string(KV)
    def __init__(self):
        super().__init__()
        self.client = asterpy.Client("cospox.com", 2345, "jamsbot", "", 1284344576730345505 )
        self._net_thread = threading.Thread(target=self.client.run)
        self._net_thread.start()
    def on_start(self):
        hist = self.client.get_history(self.client.get_channel_by_name("general"))
        for i in hist:
            self.root.ids.messages.add_widget(
                TwoLineListItem(text=f"{i.author.username}",secondary_text=f"{i.content}")
            )

    def send_message(self):
        self.client.get_channel_by_name("general").send(self.root.ids.message.text)
        self.root.ids.message.text = ""



Test().run()