import os
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

class InputPanel(GridLayout):
    Builder.load_file("{}/InputPanel.kv".format(os.path.dirname(__file__)))