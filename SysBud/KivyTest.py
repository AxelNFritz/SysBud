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
        self.row_force_default=True
        self.row_default_height=120

        self.first = SearchElement()

        self.addsear = Button(text="+ Add search element +", font_size=26)
        self.addsear.bind(on_press=self.addbutt)

        self.add_widget(self.addsear)
        self.add_widget(self.first.element)

    def addbutt(self, instance):
        self.add()
    
    def add(self):
        new = SearchElement()
        self.add_widget(new.element)

class MyApp(App):
    def build(self):
        return MyGridLayout()
 
class SearchElement(GridLayout):
    def __init__(self):

        self.element = GridLayout(cols = 1, row_force_default=True, row_default_height=30)

        self.top_grid = GridLayout(cols = 3)

        self.top_grid.add_widget(Label(text="search: "))
        self.search = TextInput(multiline=False)
        self.top_grid.add_widget(self.search)

        self.submit = Button(text="Submit", font_size=18)
        self.submit.bind(on_press=self.press)
        self.top_grid.add_widget(self.submit)

        self.element.add_widget(self.top_grid)

    def press(self, instance):
        sea = self.search.text
        if sea != "":
            res = SysSortiment.apk_search("namn1", sea)
            for row in res:
                self.element.add_widget(Label(text=f"{row}"))

if __name__ == '__main__':
    MyApp().run()
