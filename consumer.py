from number import Number
import threading

class Consomer(threading.Thread):

    def __init__(self, consomer_number: Number):
        super().__init__()
        self.consomer_number = consomer_number