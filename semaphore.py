import threading
class Semaphore:

    def __init__(self, initial_value):
        self.counter = initial_value 
        self.lock = threading.Lock() #garantir a exclusão mútua
        self.condition = threading.Condition(self.lock) #permiti que threads esperem até que o semáforo tenha recursos disponíveis
    
    def acquire(self):
        with self.condition: #recurso de contexto (semelhante ao 'using' do C#): é usado para garantir que um recurso seja liberado automaticamente, mesmo se ocorrerem exceções no bloco de código
            while self.counter <= 0:
                self.condition.wait() #esperar até que counter seja > 0
            self.counter -= 1

    def release(self):
        with self.condition:
            self.counter += 1
            self.condition.notify() #acordar quem estiver em espera (dormindo)
            