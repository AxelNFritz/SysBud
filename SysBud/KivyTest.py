import SysSortiment
import kivy
import pandas as pd
#import webbbrowser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.spinner import Spinner

class MyGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 1

        self.first = SearchElement()

        self.addsear = Button(text="+ + + Add search element + + +", font_size=20, size_hint_y = None, height = 30, on_press=self.addbutt)        
        
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

        self.spinns = SpinnElements()

        self.element = GridLayout(cols = 1, size_hint_y = None, height = 180)
        self.top_grid = GridLayout(cols = 8, size_hint_y = None, height = 30)
        self.scroll = ScrollView(do_scroll_x = False, size_hint=(1, None), size=(Window.width, 150))
        self.scrollgrid = GridLayout(cols = 1, row_force_default=True, row_default_height=30, size_hint_x = 1, size_hint_y = None, height = 3000)

        self.top_grid.add_widget(self.spinns.sea_op)

        self.search = TextInput(multiline=False)
        self.top_grid.add_widget(self.search)

        self.top_grid.add_widget(self.spinns.varugrupp)
        self.top_grid.add_widget(self.spinns.land)

        self.alt2 = (Button(text="alt2", on_press=self.allt2))
       
        self.top_grid.add_widget(self.alt2)

        self.top_grid.add_widget(self.spinns.sort_op)

        self.submit = Button(text="Submit", font_size=18, on_press=self.press)
        
        self.top_grid.add_widget(self.submit)

        self.scroll.add_widget(self.scrollgrid)
        self.element.add_widget(self.top_grid)
        self.element.add_widget(self.scroll)

    def press(self, instance):
        search_input = self.search.text
        search_land = self.spinns.land.text
        search_varugrupp = self.spinns.varugrupp.text
        search_option = self.spinns.sea_op.text 
        search_sort = self.spinns.sort_op.text
        search_target = 'namn1'

        res = SysSortiment.search(search_target, search_input, search_option, search_sort, search_varugrupp, search_land)
        for row in res:
                self.scrollgrid.add_widget(Label(text=f"{row}"))
        

    def allt2(self, instance):
        print(f'{self.spinns.varugrupp.text}  {self.spinns.land.text} {self.spinns.sort_op.text}')

class SpinnElements(GridLayout):
    def __init__(self):

        self.varugrupp_list, self.land_list = SysSortiment.get_spinner_ops()

        self.varugrupp = Spinner(text="Varugrupp",
                                values=self.varugrupp_list,
                                size_hint=(None, None),
                                size=(160, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)
        
        self.land = Spinner(text="Land",
                                values=self.land_list,
                                size_hint=(None, None),
                                size=(160, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)
        
        self.sea_op = Spinner(text="Sök",
                                values=('Sök', 'TOP'),
                                size_hint=(None, None),
                                size=(60, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)

        self.sort_op = Spinner(text="Sortering",
                                values=('Sortering', 'APK', 'prisperliter'),
                                size_hint=(None, None),
                                size=(80, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)
        


if __name__ == '__main__':
    MyApp().run()

