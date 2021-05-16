from GUIManager import GUIManager


class CalculatorManager:

    def __init__(self):
        self.__gui = GUIManager(self.num_event_handler, self.op_event_handler, self.eq_event_handler)

    def num_event_handler(self, input):
        pass

    def op_event_handler(self, input):
        pass

    def eq_event_handler(self, input):
        pass