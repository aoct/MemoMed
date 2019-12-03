import os, pickle, time

from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.properties import ObjectProperty, NumericProperty
from kivy.utils import platform
from kivy.logger import Logger
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.metrics import sp, dp
from kivy.uix.textinput import TextInput

from components.background import Background

from os.path import join

from fontScale import font_scaling


class addMedicationsPage(Screen):
	background = ObjectProperty(Background())
	font_scale = NumericProperty(1)

	def __init__(self, **kwargs):
		super(addMedicationsPage, self).__init__(**kwargs)

		if platform == 'ios': self.user_data_dir = App.get_running_app().user_data_dir
		else: self.user_data_dir = 'data'
		filename = join(self.user_data_dir, 'fontScaling.pickle')
		self.font_scale = pickle.load(open(filename, 'rb'))[0]
		self.scale_y = pickle.load(open(filename, 'rb'))[1]
		
		self.bind(size=self.size_callback)

		self.master_grid = GridLayout(cols=1, size_hint_x = 1., spacing = = font_scale(20, self.scale_y))

	def size_callback(self, instance, value):
		self.background.size = value

	def on_enter(self):
		print('MainPage')

	def elementLayoutView(self, input_text):
		row = GridLayout(cols=1, size_hint_x = .8, size_hint_y = .25)
		row.add_widget(Label(text = input_text, halign = 'center', valign = 'center', font_size = font_scaling(50, self.font_scale)))
		row.add_widget(TextInput())