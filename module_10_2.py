from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!' + '\n')
        wariors = 100
        for i in range(100):
            wariors -= self.power
            print(f'{self.name} сражается {i+1} день(дня), осталось {wariors} врагов.' + '\n')
            sleep(2)
            if wariors  < self.power:
                print(f'{self.name}, враги бежали или пали через {i+1} дней(дня)!' + '\n')

                break




first_knight = Knight('Илья Муромец', 30)
second_knight = Knight("Добрыня Никитич", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все сражения окончены!')