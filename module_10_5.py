import time
import multiprocessing

def read_info(name: str):
    all_data = []
    with open(name) as file:
        while True:
            data = file.readline()
            if not data:
                break
            all_data.append(data)


if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    start = time.time()
    for filename in filenames:
        read_info(filename)
    end = time.time()
    print(end - start, "(линейный)")
    start = time.time()
    processes = []
    for filename in filenames:
        processes.append(multiprocessing.Process(target=read_info, args=(filename,)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end = time.time()
    print(end - start, "(многопроцессный)")