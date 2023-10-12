from deposit import Deposit
from producer import Producer
from consumer import Consumer
from deposit import Deposit
from semaphore import Semaphore

permission_number = 1

mutex = Semaphore(permission_number)
full = Semaphore(0)
empty = Semaphore(permission_number)

deposit = Deposit(0, mutex, full, empty)
producer = Producer(deposit)
consumer1 = Consumer(deposit)
consumer2 = Consumer(deposit)
consumer3 = Consumer(deposit)

producer.start()
consumer1.start()
consumer2.start()
consumer3.start()
