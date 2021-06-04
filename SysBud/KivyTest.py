import SysSortiment
import kivy
import pandas as pd
#import webbbrowser
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.core.text import LabelBase
from kivy.uix.widget import Widget

from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen

class MyGridLayout(MDGridLayout):

    #LabelBase.register(name='Symbol', 
    #               fn_regular='Symbol-font.ttf')

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols=1

        self.main_grid=(MDGridLayout(cols=1))
        self.first = SearchElement()
        self.sea_element_list = [self.first]

        self.addsear = MDFloatingActionButton(icon="plus", on_press=self.addbutt, elevation_normal=6, pos_hint={"center_x": .5, "center_y": .5})
        self.btn_anchor = AnchorLayout(padding=16, anchor_x='center', anchor_y='bottom')
        self.btn_anchor.add_widget(self.addsear)

        self.add_widget(self.first.element)
        self.add_widget(self.main_grid)
        self.add_widget(self.btn_anchor)    

        
    def addbutt(self, instance):
        self.add()
    
    def add(self):
        new = SearchElement()
        self.main_grid.add_widget(new.element)
        self.sea_element_list.append(new)

class MyApp(MDApp):
    def build(self):
        return MyGridLayout()
 
class SearchElement(MDGridLayout):
    def __init__(self):
        self.hidden = True
        self.rows = 0

        self.spinns = SpinnElements()

        self.element = MDGridLayout(cols = 1, size_hint_y = None, height = 60)

        self.top_grid = MDGridLayout(cols = 8, size_hint_y = None, height = 30)
        self.scroll = ScrollView(do_scroll_x = False, size_hint=(1, None), size=(Window.width, 0))
        self.scrollgrid = MDGridLayout(cols = 8, row_force_default=True, row_default_height=25, size_hint_x = 1, size_hint_y = None, height = 0)
        
        self.show_hide_grid = MDGridLayout(cols = 1, size_hint_y = None, height = 30)
        self.show_hide_btn = Button(text="Show", font_size=18, on_press=self.show_hide)
        self.show_hide_grid.add_widget(self.show_hide_btn)

        self.top_grid.add_widget(self.spinns.sea_op)

        self.search = TextInput(multiline=False)
        self.top_grid.add_widget(self.search)

        self.top_grid.add_widget(self.spinns.varugrupp)
        self.top_grid.add_widget(self.spinns.land)

        self.top_grid.add_widget(self.spinns.sort_op)

        self.submit = Button(text="Submit", font_size=18, on_press=self.press)
        
        self.top_grid.add_widget(self.submit)

        self.scroll.add_widget(self.scrollgrid)

        self.element.add_widget(self.top_grid)
        self.element.add_widget(self.scroll)
        self.element.add_widget(self.show_hide_grid)

    def press(self, instance):
        input = self.search.text # Too add -> If "" dont search
        land = self.spinns.land.text
        varugrupp = self.spinns.varugrupp.text
        option = self.spinns.sea_op.text 
        sort = self.spinns.sort_op.text
        target = 'namn1'

        res = SysSortiment.search(target, input, option, sort, varugrupp, land)
        
        self.present_search(res, land, varugrupp, option, sort)

        self.hidden = True
        self.show_hide(self)

    def show_hide(self, instance):
        if self.hidden:
            y = self.rows * 25
            yx = y if y <= 250 else 250   # result = x if a > b else y    
            self.element.height=(yx+60)
            self.show_hide_btn.text="Hide"
            self.scroll.size=(Window.width, yx)
            self.hidden = False
        else:
            self.element.height=60
            self.show_hide_btn.text="Show"
            self.scroll.size=(Window.width, 0)
            self.hidden = True


    def allt2(self, instance):
        print(f'{self.spinns.varugrupp.text} {self.spinns.land.text} {self.spinns.sort_op.text}')

    def present_search(self, result_list, land, varugrupp, option, sort):    # Does not work, needs to be class/clasees
        
        for row in result_list:
            self.rows +=1
            self.scrollgrid.height += 25
            self.scrollgrid.add_widget(MDLabel(text=f"{row[0]}", halign='center', size_hint_x = None, width = 90)) #0, 1, 6, 9, 4, 12 Lägg till pris?
            self.scrollgrid.add_widget(MDLabel(text=f"{row[1]}", halign='center'))
            self.scrollgrid.add_widget(MDLabel(text=f"{row[6]}, {row[7]}", halign='center'))
            self.scrollgrid.add_widget(MDLabel(text=f"{row[9]}", halign='center', size_hint_x = None, width = 180))
            self.scrollgrid.add_widget(MDLabel(text=f"{row[4]}cl", halign='center', size_hint_x = None, width = 70))
            self.scrollgrid.add_widget(MDLabel(text=f"{round(row[12], 3)}", halign='center', size_hint_x = None, width = 70))
            self.scrollgrid.add_widget(Button(text="I", size_hint_x = None, width = 30, on_press=lambda instance: self.info(instance, row)))
            self.scrollgrid.add_widget(Button(text="X", size_hint_x = None, width = 30))
            #print(row)

    def info(self, instance, row):
        print(f'{row}')

#class presentElement(MDGridLayout):
#    def _init__(self):
#        self.element


class SpinnElements(MDGridLayout):
    def __init__(self):

        self.varugrupp_list, self.land_list = SysSortiment.get_spinner_ops()

        self.varugrupp = Spinner(text="Varugrupp",
                                values=self.varugrupp_list,
                                size_hint=(None, None),
                                size=(200, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)
        
        self.land = Spinner(text="Land",
                                values=self.land_list,
                                size_hint=(None, None),
                                size=(180, 30),
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

