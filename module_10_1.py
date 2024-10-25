import time
from threading import Thread
def write_words(word_count, file_name):
    with open(file_name,'w') as f:
        for i in range(1,word_count+1):
            f.write(f"Какое-то слово №{i}")
            time.sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

l = [
    (10, 'example1.txt'),
    (30, 'example2.txt'),
    (200, 'example3.txt'),
    (100, 'example4.txt'),
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt'),
]

start = time.time()
for e in l[:4]:
    write_words(*e)
end = time.time()
print(f'Работа потоков: {end-start}')

start = time.time()
thread_list = []
for e in l[4:]:
    thread_list.append(Thread(target=write_words, args=e))
for e in thread_list:
    e.start()
for e in thread_list:
    e.join()
end = time.time()
print(f'Работа потоков: {end-start}')