import os, sys
__version__ = "0.0.1"
import kivy
kivy.require("1.10.0")
from kivy.utils import platform

if platform != 'ios' and platform != 'android':
	print('Showing a smartphone-like screen')
	from kivy.config import Config
	# screen_ratio = 19.5/9 #iPhoneX
	screen_ratio = 17.5/9
	y = 360
	print('Screen size: {} : {:.0f}'.format(y, y*screen_ratio))
	Config.set('graphics', 'width', str(int(y)))
	Config.set('graphics', 'height', str(int(y*screen_ratio)))

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.core.window import Window

from openingPage import openingPage
from mainPage import mainPage
from medicationsPage import medicationsPage
from performancePage import performancePage

from fontScale import scaling


class MemoMedApp(App):
	def build(self):
		self.sm = ScreenManager(transition = NoTransition())

		scaling(Window.size)

		self.openingPage = openingPage(name = 'OpeningPage')
		self.mainPage = mainPage(name = 'MainPage')
		self.medicationsPage = medicationsPage(name = 'MedicationsPage')
		self.performancePage = performancePage(name = 'PerformancePage')
		
		self.sm.add_widget(self.openingPage)
		self.sm.add_widget(self.mainPage)
		self.sm.add_widget(self.medicationsPage)
		self.sm.add_widget(self.performancePage)		


		return self.sm

if __name__ == "__main__":
	memoMed = MemoMedApp()
	memoMed.run()