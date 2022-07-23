import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from old.grid import MyGrid
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    calc = ObjectProperty(None)
    def btn(self):
        answer = eval(self.calc.text)
        self.calc.text = str(answer)
    def remove(self):
        Remove_Last = self.calc.text[:-1]
        self.calc.text =Remove_Last
class calcApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    calcApp().run()