from kivy.app import App
from kivy.lang import Builder

class distanceConverter(App):
    def build(self):
        self.title = "Distance converter"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

distanceConverter().run()
