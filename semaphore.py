import threading
class Semaphore:

    def __init__(self, initial_value):
        self.counter = initial_value
        self.mutex = threading.Lock()
        self.condition = threading.Condition(self.mutex)
    
    def P(self):
        with self.condition:
            while self.counter <= 0:
                self.condition.wait()
            self.counter -= 1

    def V(self):
        with self.condition:
            self.counter += 1
            self.condition.notify()
            