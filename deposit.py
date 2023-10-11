from semaphore import Semaphore

class Deposit:

    def __init__(self, number: Semaphore, mutex: Semaphore, full: Semaphore, empty: Semaphore):
        self.number = number
        self.mutex = mutex
        self.full = full
        self.empty = empty

    def consume(self, thread_id):
        self.full.P()
        self.mutex.P()
        print(f"Consumidor {thread_id} consumiu: {self.number}")

        self.mutex.V()
        self.empty.V()
        return self.number
    
    def storing(self, thread_id, value):
        
        self.empty.P()
        self.mutex.P()

        self.number = value
        print(f"Produtor {thread_id} produziu: {value}")

        self.mutex.V()
        self.full.V()