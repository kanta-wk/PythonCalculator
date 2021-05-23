import os
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'exit_on_escape', '0')
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

    def __init__(self, event_num=None, event_op=None, event_eq=None, event_dec=None, event_ac=None):
        self.__event_num = event_num
        self.__event_op = event_op
        self.__event_eq = event_eq
        self.__event_dec = event_dec
        self.__event_ac = event_ac
        super().__init__()

    def build(self):
        self.__app = Calculator()
        return self.__app

    def display_main(self, message):
        self.__app.display_main(message)

    @property
    def widgets(self):
        return self.__app

    def number_button_on_press(self, send_data=None):
        self.__call_event_handler(self.__event_num, send_data)

    def operator_button_on_press(self, send_data=None):
        self.__call_event_handler(self.__event_op, send_data)

    def decimal_button_on_press(self, send_data=None):
        self.__call_event_handler(self.__event_dec, send_data)

    def ac_button_on_press(self, send_data=None):
        self.__call_event_handler(self.__event_ac, send_data)

    def equal_button_on_press(self, send_data=None):
        self.__call_event_handler(self.__event_eq, send_data)

    def __call_event_handler(self, handler, send_data):
        if(handler):
            handler(send_data)

    def set_event_num(self, handler):
        self.__event_num = handler

    def set_event_dec(self, handler):
        self.__event_dec = handler

    def set_event_op(self, handler):
        self.__event_op = handler

    def set_event_equal(self, handler):
        self.__event_eq = handler

    def set_event_ac(self, handler):
        self.__event_ac = handler

    event_num = property(fset=set_event_num)
    event_dec = property(fset=set_event_dec)
    event_op = property(fset=set_event_op)
    event_equal = property(fset=set_event_equal)
    event_ac = property(fset=set_event_ac)

if __name__ == '__main__':
    CalculatorApp().run()