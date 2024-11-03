import time
from threading import Thread
class Knight(Thread):
    name: str
    power: int
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        days_gone = 1
        for enemies_amount in range(100 - self.power, 0, -self.power):
            print(f"{self.name} сражается {days_gone}..., осталось {enemies_amount} воинов.")
            days_gone += 1
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days_gone} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()