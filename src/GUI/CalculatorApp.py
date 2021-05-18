from kivy.config import Config
Config.set('graphics', 'resizable', False)
# Config.set('modules', 'showborder', '')#TODO デバッグ用
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from InputPanel import InputPanel
from Display import Display

class CalculatorApp(App):
    Builder.load_file("./Calculator.kv")
    WIDTH = 500
    HEIGHT = 700
    Window.size = (WIDTH, HEIGHT)

if __name__ == '__main__':
    CalculatorApp().run()