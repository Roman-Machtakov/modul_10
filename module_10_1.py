import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

start_time = time.time()
threads = []
for file_name, word_count in [('example5.txt', 10), ('example6.txt', 30), ('example7.txt', 200), ('example8.txt', 100)]:
    t = threading.Thread(target=write_words, args=(word_count, file_name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()
print(f"Работа потоков {end_time - start_time:.6f} секунд")