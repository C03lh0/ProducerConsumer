from deposit import Deposit
import threading
import time

class Producer(threading.Thread):

    def __init__(self, deposit: Deposit):
        super().__init__()
        self.deposit = deposit

    def run(self):
        for i in range(0, 10):
            try:
                self.deposit.storing(self.getName(), i)
                time.sleep(0.1)
            except InterruptedError as erro:
                print(f"Erro: {erro}")


