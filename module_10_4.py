import random
import time
from threading import Thread
from queue import Queue
from typing import Unpack
class Guest(Thread):
    name: str
    def __init__(self, name: str):
        Thread.__init__(self)
        self.name = name

    def run(self):
        waiting_time = random.randint(3, 10)
        time.sleep(waiting_time)

class Table:
    number: int
    guest: Guest
    def __init__(self, number):
        self.number = number
        self.guest = None

class Cafe:
    queue: Queue[Guest]
    tables: tuple[Table]
    def __init__(self, *tables: Unpack[tuple[Table]]):
        self.tables = tables
        self.queue = Queue()
    def guest_arrival(self, *guests: Unpack[tuple[Guest]]):
        guests_list = list(guests)
        for table in self.tables:
            if table.guest == None:
                table.guest = guests_list.pop()
                print(f"{table.guest.name} сел(-а) за стол номер {table.number}")
            if len(guests_list) == 0:
                break
        for guest in guests_list:
            self.queue.put_nowait(guest)
            print(f"{guest.name} в очереди")

    def is_any_table_occupied(self):
        for table in self.tables:
            if table.guest != None:
                return True
        return False

    def discuss_guests(self):
        while not self.queue.empty() and self.is_any_table_occupied():
            for table in self.tables:
                guest: Guest = table.guest
                if guest != None and guest.is_alive():
                    continue
                if guest != None and not guest.is_alive():
                    print(f"{guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None
                if not self.queue.empty():
                    new_guest = self.queue.get()
                    table.guest = new_guest
                    print(f"{new_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                    new_guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

