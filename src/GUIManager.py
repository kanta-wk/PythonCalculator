from kivy.clock import Clock
from kivy.core.window import Window
try:
    from .GUI.CalculatorApp import CalculatorApp
except ModuleNotFoundError:
    from GUI.CalculatorApp import CalculatorApp

class GUIManager:

    def __init__(self, event_num=None, event_op=None, event_eq=None):
        self.__app = CalculatorApp()
        self.__update = False

    def output_main(self, text):
        self.set_main_string(text)

    def output_sub(self, text):
        self.set_sub_string(text)

    def app_run(self):
        self.__app.run()

    def app_end(self):
        self.__app.stop()
        Window.close()

    @staticmethod
    def set_schedule_interval(func, interval):
        Clock.schedule_interval(func, interval)

    @staticmethod
    def set_schedule_once(func, after):
        Clock.schedule_once(func, after)

    def get_main_string(self):
        return self.__app.widgets.main_string

    def set_main_string(self, text):
        self.__app.widgets.main_string = text

    def del_main_string(self):
        self.__app.widgets.main_string = ""

    def get_sub_string(self):
        return self.__app.widgets.sub_string

    def set_sub_string(self, text):
        self.__app.widgets.sub_string = text

    def del_sub_string(self):
        self.__app.widgets.sub_string = ""

    main_string = property(get_main_string, set_main_string, del_main_string, "メイン表示部の文字列")
    sub_string = property(get_sub_string, set_sub_string, del_sub_string, "サブ表示部の文字列")

if __name__ == '__main__':
    from functools import partial
    gui = GUIManager()

    def main_test(text, *args):
        gui.output_main(text)

    def sub_test(text, *args):
        gui.output_sub(text)

    gui.set_schedule_once(partial(main_test, "called"), 2)
    gui.set_schedule_once(partial(sub_test, "called"), 3)
    gui.app_run()