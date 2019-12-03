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

import threading
from functools import partial

class openingPage(Screen):
	background = ObjectProperty(Background())

	def __init__(self, **kwargs):
		super(openingPage, self).__init__(**kwargs)
		self.bind(size=self.size_callback)

	def size_callback(self, instance, value):
		self.background.size = value

	def on_enter(self):
		mythread = threading.Thread(target = partial(self.loading))
		mythread.start()

	def loading(self):
		start_time = time.time()
		while time.time() - start_time < 1: pass
		App.get_running_app().sm.current = 'MainPage'

Builder.load_string("""
<openingPage>:
	background: background
	Background:
		id: background
		pos: root.pos
	Image:
		source: 'images/MemoMedLogo.png'
		background_color: 0, 0, 0, .0
		size_hint: (.3, .3)

	""")