from semaphore import Semaphore

class Deposit:

    def __init__(self, number, mutual_exclusion: Semaphore, full: Semaphore, empty: Semaphore):
        self.number = number
        self.mutual_exclusion = mutual_exclusion #semáforo mutex - garante que apenas um thread acesse uma região crítica por vez
        self.full = full #semáforo full - indica se a região crítica(depósito) está cheia, ou seja, se há algo para consumir
        self.empty = empty #semáforo empity - indica se a região crítica(depósito) está vazia, ou seja, se há espaço para produzir

    def consume(self, thread_id):
        self.full.acquire() #se estiver cheio, consome, se não aguarda
        self.mutual_exclusion.acquire() #garante acesso ao depósito

        print(f"Consumidor {thread_id} consumiu: {self.number}")

        self.mutual_exclusion.release() #libera o acesso ao depósito
        self.empty.release() #notifica que o depósito esta vazia
        return self.number
    
    def produce(self, thread_id, value):
        self.empty.acquire() #se estiver vazio, produz, se não aguarda
        self.mutual_exclusion.acquire() #garante acesso ao depósito

        self.number = value 
        print(f"Produtor {thread_id} produziu: {value}")

        self.mutual_exclusion.release() #libera o acesso ao depósito
        self.full.release() #notifica que o depósito esta cheio