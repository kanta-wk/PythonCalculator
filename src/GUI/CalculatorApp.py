import os
from kivy.config import Config
Config.set('graphics', 'resizable', False)
# Config.set('modules', 'showborder', '')#TODO デバッグ用
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
try:
    from .InputPanel import InputPanel
    from .Display import Display
except ModuleNotFoundError:
    from InputPanel import InputPanel
    from Display import Display

class Calculator(BoxLayout):
    main_display = ObjectProperty(None)
    sub_display = ObjectProperty(None)

    def get_main_string(self):
        return self.main_display.text

    def set_main_string(self, text):
        self.main_display.text = text

    def get_sub_string(self):
        return self.sub_display.text

    def set_sub_string(self, text):
        self.sub_display.text = text

    main_string = property(get_main_string, set_main_string)
    sub_string = property(get_sub_string, set_sub_string)

class CalculatorApp(App):
    WIDTH = 500
    HEIGHT = 700
    Window.size = (WIDTH, HEIGHT)
    def build(self):
        self.__app = Calculator()
        return self.__app

    def display_main(self, message):
        self.__app.display_main(message)

    @property
    def widgets(self):
        return self.__app

if __name__ == '__main__':
    CalculatorApp().run()