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

class performancePage(Screen):
	background = ObjectProperty(Background())
	font_scale = NumericProperty(1)

	def __init__(self, **kwargs):
		super(performancePage, self).__init__(**kwargs)

		if platform == 'ios': self.user_data_dir = App.get_running_app().user_data_dir
		else: self.user_data_dir = 'data'
		self.font_scale = pickle.load(open(join(self.user_data_dir, 'fontScaling.pickle'), 'rb'))[0]
		
	def size_callback(self, instance, value):
		self.background.size = value

	def on_enter(self):
		print('Performance Page')

Builder.load_string("""
<performancePage>:
	background: background
	Background:
		id: background
		pos: root.pos

	Button:
		on_release: app.sm.current = 'MainPage'
		size_hint: (.1, .1)
		pos_hint: {'x': 0.01, 'y': .89}
		text: 'home'

	""")