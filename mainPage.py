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

from components.background import Background

from os.path import join

from fontScale import font_scaling

class mainPage(Screen):
	background = ObjectProperty(Background())
	font_scale = NumericProperty(1)

	def __init__(self, **kwargs):
		super(mainPage, self).__init__(**kwargs)

		if platform == 'ios': self.user_data_dir = App.get_running_app().user_data_dir
		else: self.user_data_dir = 'data'
		self.font_scale = pickle.load(open(join(self.user_data_dir, 'fontScaling.pickle'), 'rb'))[0]
		print('here')
		self.bind(size=self.size_callback)

	def size_callback(self, instance, value):
		self.background.size = value

	def on_enter(self):
		print('MainPage')


Builder.load_string("""
<mainPage>:
	background: background
	Background:
		id: background
		pos: root.pos
	Button:
		on_release: app.sm.current = 'MedicationsPage'
		size_hint: (.8, .3)
		pos_hint: {'x': .1,'y': .55}
		background: 0, 0, 0, .0
		text: 'Medications Page'
	Button:
		on_release: app.sm.current = 'PerformancePage'
		size_hint: (.8, .3)
		pos_hint: {'x':.1, 'y': .05}
		background: 0, 0, 0, .0
		text: 'Performance Page'

	""")
