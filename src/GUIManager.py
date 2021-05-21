from kivy.clock import Clock
from kivy.core.window import Window
try:
    from .GUI.SendCharacters import SendCharacters
    from .GUI.CalculatorApp import CalculatorApp as GuiApp
except ModuleNotFoundError:
    from GUI.SendCharacters import SendCharacters
    from GUI.CalculatorApp import CalculatorApp as GuiApp

class GUIManager(SendCharacters):

    def __init__(self, event_num=None, event_op=None, event_eq=None, event_dec=None, event_ac=None):
        self.__app = GuiApp(event_num=event_num, event_dec=event_dec, event_op=event_op, event_eq=event_eq, event_ac=event_ac)
        self.__update = False

    def output_main(self, text):
        self.main_string = text

    def output_sub(self, text):
        self.sub_string = text

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

    def set_event_num(self, handler):
        self.__app.event_num = handler

    def set_event_dec(self, handler):
        self.__app.event_dec = handler

    def set_event_op(self, handler):
        self.__app.event_op = handler

    def set_event_equal(self, handler):
        self.__app.event_equal = handler

    def set_event_ac(self, handler):
        self.__app.event_ac = handler


    main_string = property(get_main_string, set_main_string, del_main_string, "メイン表示部の文字列")
    sub_string = property(get_sub_string, set_sub_string, del_sub_string, "サブ表示部の文字列")
    event_num = property(fset=set_event_num)
    event_dec = property(fset=set_event_dec)
    event_op = property(fset=set_event_op)
    event_equal = property(fset=set_event_equal)
    event_ac = property(fset=set_event_ac)

if __name__ == '__main__':
    from functools import partial
    gui = GUIManager()



    # def main_test(text, *args):
    #     gui.output_main(text)
    #
    # def sub_test(text, *args):
    #     gui.output_sub(text)
    #
    # gui.set_schedule_once(partial(main_test, "called"), 2)
    # gui.set_schedule_once(partial(sub_test, "called"), 3)

    def display_main(input):
        gui.output_sub(gui.main_string)
        gui.output_main(input)

    gui.event_num = display_main
    gui.event_dec = display_main
    gui.event_equal = display_main
    gui.event_ac = display_main
    gui.event_op = display_main

    gui.app_run()