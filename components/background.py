from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.vector import Vector

from kivy.core.window import Window

class Background(Widget):
	image = ObjectProperty(Image())

	def __init__(self, **kwargs):
		super(Background, self).__init__(**kwargs)
		self.image.pos = (0,0)

Builder.load_string("""
<Background>:
	image: image
	Image:
		id: image
		allow_stretch: True
		source: "images/background/standard.png"
		size: root.height*self.image_ratio, root.height
	""")