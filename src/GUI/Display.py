from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import StringProperty

class Display(Widget):
    Builder.load_file("./Display.kv")
    text = StringProperty("")

if __name__ == '__main__':
    from kivy.app import App
    class Test(App):
        def build(self):
            return Display()

    Test().run()
