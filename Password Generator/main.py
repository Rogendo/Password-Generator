import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
import random

# loading your .kv file
Builder.load_file('my.kv') 

class MyLayout(Widget):
	def on_click(self):
		lower="abcdefghijklmnopqrstuvwxyz"
		upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		numbers="0123456789"
		symbols="!@#$%^&*()."
		string= lower+upper+numbers+symbols
		length=16
		password="".join(random.sample(string,length))
		self.ids.lebel_1.text=password
		print("Your new PASSWORD is:" +password)


class PasswordGeneratorApp(App):
	def build(self):
		# Window.clearcolor=(1,1,1,1)
		return MyLayout()

if __name__ == '__main__':
	PasswordGeneratorApp().run()