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
from kivy.uix.popup import Popup

from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatIconButton
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField, MDTextFieldRect, MDTextFieldRound

from kivy.graphics import Color, Rectangle
from kivy.utils import get_color_from_hex


class MyGridLayout(MDGridLayout):

    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols=1

        self.main_grid=(MDGridLayout(cols=1))
        self.first = SearchElement()
        self.c = []
        self.c.append(self.first)

        self.addsear = MDFloatingActionButton(icon="plus", on_press=self.addbutt, elevation_normal=6, pos_hint={"center_x": .5, "center_y": .5})
        self.btn_anchor = AnchorLayout(padding=16, anchor_x='center', anchor_y='bottom')
        self.btn_anchor.add_widget(self.addsear)

        #self.add_widget(self.first.element)
        self.add_widget(self.main_grid)
        self.main_grid.add_widget(self.first.element)
        self.add_widget(self.btn_anchor)    

        
    def addbutt(self, instance):
        self.add()
    
    def add(self):
        new = SearchElement()
        self.main_grid.add_widget(new.element)
        self.c.append(new)

class MyApp(MDApp):
    def build(self):
        return MyGridLayout()
 
class SearchElement(MDGridLayout):
    def __init__(self):
        self.hidden = True
        self.rows = 0
        self.row_o_list = []

        self.element = MDGridLayout(cols = 1, size_hint_y = None, height = 60)

        self.top_grid = MDGridLayout(cols = 8, size_hint_y = None, height = 30)
        self.scroll = ScrollView(do_scroll_x = False, size_hint=(1, None), size=(Window.width, 0))
        self.scrollgrid = MDGridLayout(cols = 1, row_force_default=True, row_default_height=25, size_hint=(1, None), height = 0, padding=[5,0])
        
        #self.scrollgrid.canvas.add(Color(rgb=get_color_from_hex("#39B3F2")))
        #self.scrollgrid.canvas.add(Rectangle(size=(20, 25), pos=(50, 50))) #self.scrollgrid.pos))
        #2000, 25*100
        
        self.show_hide_grid = MDGridLayout(cols = 1, size_hint_y = None, height = 30)
        self.show_hide_btn = Button(text="Show", font_size=18, on_press=self.show_hide)
        self.show_hide_grid.add_widget(self.show_hide_btn)

        

        self.search = MDTextFieldRect(hint_text='Sök dryck') #, height=10, pos=(0, 20))

        self.spinns = SpinnElements(self.search)

        self.top_grid.add_widget(self.spinns.sea_op)

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
        
        #rader = len(result_list)
        #canvas.before=(Color=(rgba=[.5,.5,.5,1]), Line=(width=2, rectangle=(self.x, self.y, self.width, self.height))
        #self.rows +=1
        #self.scrollgrid.height += 25
        #self.scrollgrid.add_widget(MDLabel(text=f"Artkl.nr: ", size_hint_x = None, width = 90)) #0, 1, 6, 9, 4, 12 Lägg till pris?
        #self.scrollgrid.add_widget(MDLabel(text=f"Namn: "))
        #self.scrollgrid.add_widget(MDLabel(text=f"Stil: "))
        #self.scrollgrid.add_widget(MDLabel(text=f"Land: ", size_hint_x = None, width = 180))
        #self.scrollgrid.add_widget(MDLabel(text=f"Volym: ", size_hint_x = None, width = 70))
        #self.scrollgrid.add_widget(MDLabel(text=f"APK: ", size_hint_x = None, width = 70))
        #self.scrollgrid.add_widget(MDLabel(text="Rader:", size_hint_x = None, width = 45))
        #self.scrollgrid.add_widget(MDLabel(text=f"{rader}", size_hint_x = None,  width = 35, halign='center'))

        for row in result_list:
            self.rows +=1
            self.scrollgrid.canvas.before.add(Color(rgb=get_color_from_hex("#d3d3d3")))
            self.scrollgrid.canvas.before.add(Rectangle(size=(2500, 23), pos=(0, ((self.rows*25) -24 ))))
            self.scrollgrid.height += 25
            
            self.new_o = PresentResult(row, self)
            self.row_o_list.append(self.new_o)
            
            self.scrollgrid.add_widget(self.new_o.p_element)

    def info(self, instance, row):
        print(f'{row}')


class PresentResult(MDGridLayout):
    def __init__(self, result_row, object):

        self.p_element = MDGridLayout(cols = 8)

        self.p_element.add_widget(MDLabel(text=f"{result_row[0]}", size_hint_x = None, width = 90)) #0, 1, 6, 9, 4, 12 Lägg till prijacs?
        self.p_element.add_widget(MDLabel(text=f"{result_row[1]}"))
        self.p_element.add_widget(MDLabel(text=f"{result_row[6]}, {result_row[7]}"))
        self.p_element.add_widget(MDLabel(text=f"{result_row[9]}", size_hint_x = None, width = 180))
        self.p_element.add_widget(MDLabel(text=f"{result_row[4]}cl", size_hint_x = None, width = 70))
        self.p_element.add_widget(MDLabel(text=f"{round(result_row[12], 3)}", size_hint_x = None, width = 70))
        self.p_element.add_widget(Button(text="I", size_hint_x = None, width = 40, on_press=lambda instance: self.info(instance, result_row))) 
        self.p_element.add_widget(Button(text="X", size_hint_x = None, width = 40, on_press=lambda instance: rem(self, instance))) 
        

        def rem(self, instance):
            self.p_element.parent.remove_widget(self.p_element)
            object.scrollgrid.height -= 25
            object.rows -= 1

    def info(self, instance, result_row):
        i_element = MDGridLayout(cols = 2)

        i_texts = ['Artikel Nr','Namn1','Namn2','Pris','Volym(ml)','Kr/Liter','Varugrupp','Typ','Stil','Land','Producent','Alk(%)','APK']
        for i in range(len(result_row)):
            i_element.add_widget(MDLabel(text=f'{i_texts[i]}: ', theme_text_color="Custom", text_color=[.8, 1, 1, 1]))
            i_element.add_widget(MDLabel(text=f"{result_row[i]}", theme_text_color="Custom", text_color=[.8, 1, 1, 1]))

        popup = Popup(title=f'{result_row[1]} full information',
                    content=i_element,
                    size_hint=(None, None), size=(350, 500))
        
        popup.open()
        

class SpinnElements(MDGridLayout):
    def __init__(self, object):

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
        
        def sea_op_dep(spinner, text):
            if self.sea_op.text == 'Sök':
               object.hint_text = 'Sök dryck'
            else:
               object.hint_text = 'Ange rader'
        
        self.sea_op.bind(text=sea_op_dep)

        self.sort_op = Spinner(text="Sortering",
                                values=('Sortering', 'APK', 'prisperliter'),
                                size_hint=(None, None),
                                size=(80, 30),
                                pos_hint={'center_x': .5, 'center_y': .5},
                                sync_height=True)

        

if __name__ == '__main__':
    MyApp().run()

