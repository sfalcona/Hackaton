from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Line
from kivy.clock import Clock
from kivy.graphics import *
from kivy.config import Config
from kivy.properties import StringProperty, NumericProperty, ListProperty

from qrcode import createCode
import requests



Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 50)
Config.set('graphics', 'top',  50)
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')


class MainScreen(Screen):
	def __init__(self,**kwargs):
            super(MainScreen, self).__init__(**kwargs)

	def buttonCallback(self):
		pass
	def loadCallback(self):
		self.parent.current = "load"
    	
	def payCallback(self):
		self.parent.current = "pay"

   
class LoadScreen(Screen):
	def buttonCallback(self):
		self.parent.current = "main"
	def saveData(self):
		with open("items.txt","a") as f:
			f.write(self.nameT.text + ' ' +
					self.priceT.text + ' ' +
					self.infoT.text + ' ' +
					str(self.diabT.active) + ' ' +
					str(self.celT.active) + ' ' +
					str(self.pict.selection) +'\n')
		self.parent.current = "main"

class PayScreen(Screen):
	def callback(self):
		print('Me llego un enter')
	
	def on_pre_enter(self, *args):

		def callback(value):
			self.parent.tot += int(value.text) * int(value.id)
			# print(value.text + value.id)

		c = 65
		layout = GridLayout(cols = 4, spacing='1dp', size_hint_x = 0.9, pos= (0, self.parent.height))
		self.ids.scroll.clear_widgets()
		with open('items.txt') as f:
			mylist = [line.rstrip('\n') for line in f]
		for item in mylist:
			data = item.split()
			lbl1 = Label(text=data[0], size_hint=(.4, 1), color = [0,0,0,1])
			lbl2 = Label(text=data[1], size_hint=(.4, 1), color = [0,0,0,1])
			wimg = Image(source=data[-1][2:-2], size_hint=(0.2,1))
			textinput = TextInput(id = data[1], hint_text='0', size_hint=(0.1,1), multiline = False)
			textinput.bind(on_text_validate = callback)
			c += 1
			layout.add_widget(lbl1)
			layout.add_widget(lbl2)
			layout.add_widget(wimg)
			layout.add_widget(textinput)
		self.ids.scroll.add_widget(layout)
	def buttonCallback(self):
		self.parent.current = "main"


	def cobrar(self):
		r = requests.post("http://127.0.0.1/", data={self.nombre.text: self.parent.tot})
		# for i in range(65,self.c):
		# 	print(i)
		# 	print(getattr(self, chr(i)).text)
		# with open('items.txt') as f:
		# 	mylist = [line.rstrip('\n') for line in f]
		# print(saldo)
		

class ScreenManagement(ScreenManager):
	it = ListProperty([])
	tot = NumericProperty(0)
    


class MainApp(App):
    def build(self):
        return presentation
    

presentation = Builder.load_file('empresa.kv')
	
if __name__ == "__main__":
    MainApp().run()
		
