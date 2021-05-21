import os
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder

from SendCharacters import SendCharacters


class InputPanel(GridLayout, SendCharacters):
    Builder.load_file("{}/InputPanel.kv".format(os.path.dirname(__file__)))