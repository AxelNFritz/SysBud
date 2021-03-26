import SysSortiment
import kivy
import pandas as pd
#import webbbrowser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
 


class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="search: "))
        self.search = TextInput(multiline=False)
        self.add_widget(self.search)

        self.submit = Button(text="Submit", font_size=28)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        search = self.search.text
        res = SysSortiment.apk_search("namn1", search)
        for row in res:
            self.add_widget(Label(text=f"{row}"))

class MyApp(App):
    def build(self):
        return MyGridLayout()
 

if __name__ == '__main__':
    MyApp().run()
