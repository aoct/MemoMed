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
from kivy.uix.scrollview import ScrollView

from components.background import Background

from os.path import join

from fontScale import font_scaling

all_medications = ['med']

class medicationsPage(Screen):
	background = ObjectProperty(Background())
	font_scale = NumericProperty(1)

	def __init__(self, **kwargs):
		super(medicationsPage, self).__init__(**kwargs)

		if platform == 'ios': self.user_data_dir = App.get_running_app().user_data_dir
		else: self.user_data_dir = 'data'
		filename_font = join(self.user_data_dir, 'fontScaling.pickle')
		self.font_scale = pickle.load(open(filename_font, 'rb'))[0]
		self.scale_y = pickle.load(open(filename_font, 'rb'))[1]
		
		self.bind(size=self.size_callback)

		self.master_grid = GridLayout(cols=1,
									   size_hint=(1.,.8),
									   pos_hint={'x':0., 'y':.05},
									   )
		self.medications_list = GridLayout(cols=1, size_hint_x=1., spacing=font_scaling(20, self.scale_y))
		self.medications_list.add_widget(Label(text = 'Medications', bold =True, font_size = font_scaling(70, self.font_scale), size_hint_y = .25))
		
		self.medications_ScrollView = ScrollView(size_hint=(1., .9))
		filename = join(self.user_data_dir, 'medications.pickle')
		if os.path.isfile(filename):
			global all_medications
			all_medications = pickle.load(open(filename, 'rb'))

		for med in all_medications:	
			row = GridLayout(cols=3, size_hint_y=.25)
			row.add_widget(Label(text='MED NAME', size_hint_x = 0.48, size_hint_y = 1))
			row.add_widget(Label(text='DOSING', size_hint_x = 0.23, size_hint_y = 1))
			row.add_widget(Button(text = 'EDIT', size_hint_x = 0.23, size_hint_y = 1))

		self.master_grid.add_widget(self.medications_list)
		self.add_widget(self.master_grid)


	def size_callback(self, instance, value):
		self.background.size = value

	def on_enter(self):
		print('MainPage')


	def elementLayoutView(self, input_text):
		row = GridLayout(cols=1, size_hint_x = .8, size_hint_y = .25)
		row.add_widget(Label(text = input_text, halign = 'center', valign = 'center', font_size = font_scaling(50, self.font_scale)))
		row.add_widget(TextInput())

Builder.load_string("""
<medicationsPage>:
	background: background
	Background:
		id: background
		pos: root.pos
	Button:
		on_release: app.sm.current = 'MainPage'
		size_hint: (.1, .1)
		pos_hint: {'x': 0.01, 'y': .89}
		text: 'Home'

	""")