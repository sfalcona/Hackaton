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
        self.parent.current = "other"

class AnotherScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
    pass




class MainApp(App):
    def build(self):
        return presentation
    def printalgo(self):
    	print("algo")

if __name__ == "__main__":
    MainApp().run()
		
		