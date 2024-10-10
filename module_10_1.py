from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    for i in range(1, word_count + 1):
        with open(file_name, 'a', encoding='UTF-8') as file:
            file.write(f'Какое-то слово номер {i}\n')
            sleep(0.1)
    file.close()
    print(f'Запись в файл {file_name}')


time_start1 = datetime.now()
write_words(10, 'testing1.txt')
write_words(30, 'testing2.txt')
write_words(200, 'testing3.txt')
write_words(100, 'testing4.txt')
time_end1 = datetime.now()
time_res1 = time_end1 - time_start1
print(time_res1)

time_start2 = datetime.now()
func1 = Thread(target=write_words, args=(10, "testing5.txt"))
func2 = Thread(target=write_words, args=(30, "testing6.txt"))
func3 = Thread(target=write_words, args=(200, "testing7.txt"))
func4 = Thread(target=write_words, args=(100, "testing8.txt"))

func1.start()
func2.start()
func3.start()
func4.start()

func1.join()
func2.join()
func3.join()
func4.join()
time_end2 = datetime.now()
time_res2 = time_end2 - time_start2
print(time_res2)