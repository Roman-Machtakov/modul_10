import datetime
import multiprocessing
import os

def read_info(name):
    all_data = []
    with open(os.path.join(os.getcwd(), name)) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break

file_names = [f'file{number}.txt' for number in range(1, 5)]

if __name__ == "__main__":
    start1 = datetime.datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end1 = datetime.datetime.now()
    print(f'{end1 - start1} (Линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        start2 = datetime.datetime.now()
        pool.map(read_info, file_names)
        end2 = datetime.datetime.now()
    print(f'{end2 - start2} (Многопроцессорный)')