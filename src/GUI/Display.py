from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

class Display(Widget):
    Builder.load_file("./Display.kv")
    text = StringProperty("")
    font_size = NumericProperty(50)

if __name__ == '__main__':
    from kivy.app import App
    class Test(App):
        def build(self):
            return Display()

    Test().run()
