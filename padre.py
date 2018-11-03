from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Line

from kivy.clock import Clock

from kivy.graphics import *

from kivy.config import Config

Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 50)
Config.set('graphics', 'top',  50)
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '500')


class Painter(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

            
class LogoScreen(Screen):
    def __init__(self,**kwargs):
            super(LogoScreen, self).__init__(**kwargs)

    def on_enter(self, *args):
        self.displayScreenThenLeave()

    def displayScreenThenLeave(self):
        Clock.schedule_once(self.changeScreen, 1)

    def changeScreen(self, *args):
        self.parent.current = "auth"

class AnotherScreen(Screen):
    def buttonCallback(self):
        self.parent.current = "option"
        print("fui a opciones")

class OptionScreen(Screen):
    def buttonCallback(self):
        self.parent.current = "main"
        print("volvi a menu")

class AuthScreen(Screen):
    def changeScreen(self, *args):
        self.parent.current = "Home"

class HomeScreen(Screen):
    def goToCalledScreen(self, nextScreen="History"):
        self.parent.current = nextScreen

class HistoryScreen(Screen):
    def goToHomeScreen(self, *args):
        self.parent.current = "Home"

class ChargeScreen(Screen):
    def goToHomeScreen(self, *args):
        self.parent.current = "Home"

class WithdrawScreen(Screen):
    def goToHomeScreen(self, *args):
        self.parent.current = "Home"

class ScreenManagement(ScreenManager):
    pass



presentation = Builder.load_file('padre.kv')


class MainApp(App):
    def build(self):
        return presentation
    

if __name__ == "__main__":
    MainApp().run()
        
        