import random
import threading
from threading import Lock
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(10):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_int = random.randint(50, 500)
            self.balance += random_int
            print(f'Пополнение - {random_int}  Баланс - {self.balance}' + '\n')
            sleep(0.01)

    def take(self):
        for j in range(10):
            random_int = random.randint(50, 500)
            print(f'Запрос на снятие {random_int}' + '\n')
            if random_int <= self.balance:
                self.balance -= random_int
                print(f'Снятие - {random_int}  Баланс - {self.balance}' + '\n')
            else:
                print(f'Запрос отклонен,недостаточно средств' + '\n')
                self.lock.acquire()
                sleep(0.01)





bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс - {bk.balance}')