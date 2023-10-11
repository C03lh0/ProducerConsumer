from deposit import Deposit
import threading
import time

class Consomer(threading.Thread):

    def __init__(self, deposit: Deposit):
        super().__init__()
        self.deposit = deposit

    def run(self):
        value = 0
        for i in range(0, 10):
            try:
                value = self.deposit.consume(self.getName())
                time.sleep(2)
            except InterruptedError as erro:
                print(f"Erro: {erro}")

