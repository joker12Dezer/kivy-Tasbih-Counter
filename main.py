import kivy
from kivy.uix.label import Label as lb
from kivy.uix.gridlayout import GridLayout as gl
from kivy.uix.button import Button as btn
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout as fl

import time as dt

start=dt.time_ns()
con=0
class Main(App):
	
	def build(self):
		self.c=1
		home=fl()
		self.icon="Images/Bub.ico"
		back=Image(source="Images/Jerusalem.jpeg",allow_stretch=True,keep_ratio=False)
		self.clan=gl(cols=1,rows=2)
		self.mn=lb(text=str(0),font_size=92,color=(0,1,0,1),font_name=r"Fonts/digital_7/digital-7.ttf")
		self.clan.add_widget(self.mn)
		self.clan.add_widget(btn(text='click',background_color=(1,2,2,1),size_hint=(.6,.14),on_press=self.free))
		home.add_widget(back)
		home.add_widget(lb(text="Digital Tasbeeh",font_name='Fonts/valentica/valentina',font_size=74))
		home.add_widget(self.clan)
		return home
	
	def free(self,dtm):
		self.mn.text=str(self.c)
		self.c+=1
		
		
Main().run()