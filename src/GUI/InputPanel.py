import os
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.core.window import Window
from kivy.core.window import Keyboard

from SendCharacters import SendCharacters

class InputButton(Button):

    def link_button_on_press(self):
        self.dispatch("on_press")

    def link_button_on_release(self):
        self.dispatch("on_release")


class InputPanel(GridLayout, SendCharacters):
    Builder.load_file("{}/InputPanel.kv".format(os.path.dirname(__file__)))
    WITH_SHIFT = {Keyboard.keycodes[";"] : Keyboard.keycodes["+"],
                  Keyboard.keycodes[":"] : Keyboard.keycodes["*"],
                  Keyboard.keycodes["-"] : Keyboard.keycodes["enter"]}
    SIMPLE_COMVERT = {Keyboard.keycodes["numpad0"] : Keyboard.keycodes["0"],
                      Keyboard.keycodes["numpad1"] : Keyboard.keycodes["1"],
                      Keyboard.keycodes["numpad2"] : Keyboard.keycodes["2"],
                      Keyboard.keycodes["numpad3"] : Keyboard.keycodes["3"],
                      Keyboard.keycodes["numpad4"] : Keyboard.keycodes["4"],
                      Keyboard.keycodes["numpad5"] : Keyboard.keycodes["5"],
                      Keyboard.keycodes["numpad6"] : Keyboard.keycodes["6"],
                      Keyboard.keycodes["numpad7"] : Keyboard.keycodes["7"],
                      Keyboard.keycodes["numpad8"] : Keyboard.keycodes["8"],
                      Keyboard.keycodes["numpad9"] : Keyboard.keycodes["9"],
                      Keyboard.keycodes["numpaddivide"] : Keyboard.keycodes["/"],
                      Keyboard.keycodes["numpadmul"] : Keyboard.keycodes["*"],
                      Keyboard.keycodes["numpadsubstract"] : Keyboard.keycodes["-"],
                      Keyboard.keycodes["numpadadd"] : Keyboard.keycodes["+"],
                      Keyboard.keycodes["numpadenter"] : Keyboard.keycodes["enter"]}
    key_codes = Keyboard.keycodes

    def __init__(self, *args, **kwargs):
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self, input_type="text")
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        self.__app = App.get_running_app()
        self.__shift = False
        self.__ctrl = False

        super().__init__(*args, **kwargs)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        if(keycode[0] == Keyboard.keycodes["shift"] or keycode[0] == Keyboard.keycodes["rshift"]):
            self.__shift = False
        if(keycode[0] == Keyboard.keycodes["lctrl"] or keycode[0] == Keyboard.keycodes["rctrl"]):
            self.__ctrl = False
        self._button_on_release(keycode)

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if(keycode[0] == Keyboard.keycodes["shift"] or keycode[0] == Keyboard.keycodes["rshift"]):
            self.__shift = True
        if(keycode[0] == Keyboard.keycodes["lctrl"] or keycode[0] == Keyboard.keycodes["rctrl"]):
            self.__ctrl = True
        self._button_on_press(keycode)
        print(keycode)

    def _button_on_press(self, keycode):
        button = self.__search_button(keycode)
        if(button):
            button.state = "down"
            button.link_button_on_press()
            print(button.on_press)

    def _button_on_release(self, keycode):
        button = self.__search_button(keycode)
        if(button):
            button.state = "normal"
            button.link_button_on_release()

    def __search_button(self, keycode:list):
        __keycode = self.__convert_key_code(keycode)
        for widget in self.children:
            if(isinstance(widget, InputButton) and widget.keycode == __keycode):
                return widget

    def __convert_key_code(self, keycode: list):
        simple_convert = self.SIMPLE_COMVERT.get(keycode[0])
        if(simple_convert):
            return simple_convert

        shift_convert = self.WITH_SHIFT.get(keycode[0])

        if(self.__shift and shift_convert):
            return shift_convert
        return keycode[0]