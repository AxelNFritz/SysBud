#import kivy
#from KivyTest import MyGridLayout
from logging import root
import KivyTest
import SysSortiment

#from kivy.app import App
from kivymd.app import MDApp

#from kivy.uix.screenmanager import ScreenManager, Screen
#from kivymd.uix.screen import MDScreen


#from kivy.uix.gridlayout import GridLayout
#from kivy.uix.screenmanager import Screen
#from kivy.uix.button import Button
#from kivy.core.window import Window
from kivy.uix.widget import Widget

#from kivymd.uix.boxlayout import BoxLayout
#from kivy.factory import Factory
from kivymd.uix.label import MDLabel
#from kivymd.uix.gridlayout import MDGridLayout
#from kivymd.uix.button import MDFloatingActionButton, MDRectangleFlatIconButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRect, MDTextFieldRound


class MainWindow(Widget):
    pass

class MySysBudApp(MDApp):


    def on_start(self):
        self.M = KivyTest.MyGridLayout()
        self.root.ids.main_element.add_widget(self.M)
        return super().on_start()


    def build(self):
        return MainWindow()

    def screen_trans(self, sc):
        target = int(sc.name)
        home = int(self.root.ids.screen_m.current)
        dir = 'up' if target > home else 'down'
        self.root.ids.screen_m.switch_to(sc, direction = dir)


if __name__ == '__main__':
    MySysBudApp().run()