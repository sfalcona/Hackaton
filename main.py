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
from kivy.properties import StringProperty



from qrcode import createCode
import requests

validUsers = {"sebastian": "123"}
userName = []


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

class MainScreen(Screen):
    def on_enter(self, *args):
        # print(self.manager.mySaldo)
        self.updateVal()

    def updateVal(self, *args):
        r = requests.get('http://127.0.0.1/?name=' + self.manager.myName, auth=('user', 'pass'))
        mySaldo = r.text
        self.saldo.text =  'SALDO ' + mySaldo 
        Clock.schedule_once(self.updateVal, 0.5)
        print('request')

    def buttonCallback(self):
        self.parent.current = "option"
        print("fui a opciones")

class OptionScreen(Screen):
    def buttonCallback(self):
        self.parent.current = "main"
        print("volvi a menu")

class AuthScreen(Screen):
    def saveData(self):
        validUser = False
        for user, passw in validUsers.items():
            if user == self.nameT.text:
                validUser = True
                self.nameL.text = "Usuario"
                self.nameL.color = 0,0,0,1
                if passw == self.passwT.text:
                    userName = user
                    createCode(user)
                    self.manager.myName = user
                    self.parent.current = "main"
                else:
                    self.passL.text = "Contrasena Incorrecta"
                    self.passL.color = 1,0,0,1
        if not(validUser):
            self.nameL.text = "Usuario Incorrecto"
            self.nameL.color = 1,0,0,1
   
  

class ScreenManagement(ScreenManager):
    myName = StringProperty('')



presentation = Builder.load_file('main2.kv')


class MainApp(App):
    def build(self):
        return presentation
    

if __name__ == "__main__":
    MainApp().run()
		
		