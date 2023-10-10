from number import Number
import threading

class Producer(threading.Thread):

    def __init__(self, producer_number: Number):
        super().__init__()
        self.producer_number = producer_number

    


