# Завдання 1
# Створіть функцію для обчислення факторіала числа.
# Запустіть декілька завдань, використовуючи Thread,
# і заміряйте швидкість їхнього виконання,
# а потім заміряйте швидкість обчислення,
# використовуючи той же набір завдань на ThreadPoolExecutor.
# Як приклади використовуйте останні значення,
# від мінімальних і до максимально можливих, щоб побачити приріст або втрату продуктивності.


import concurrent.futures
import math
import os
import threading
import time


def find_factorial(name: str, x: int):
    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    st_time = time.time()
    fin_time = time.time() - st_time
    print(f"(for {name} result is {math.factorial(x)} get in {fin_time}")
    return math.factorial(x)


thread1 = threading.Thread(target=find_factorial, args=("First Thread", 5))
thread2 = threading.Thread(target=find_factorial, args=("Second Thread", 1000000))
thread3 = threading.Thread(target=find_factorial, args=("Third Thread", 50))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()


def find_factorial_by_thread_pool():

    # Create a ThreadPoolExecutor with a maximum of 3 worker threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks and store Future objects
        future1 = executor.submit(find_factorial, "FIrst", 5)
        future2 = executor.submit(find_factorial, "Second", 1000000)
        future3 = executor.submit(find_factorial, "Third", 50)

        # Retrieve results from the completed futures
        for future in concurrent.futures.as_completed([future1, future2, future3]):
            try:
                result = future.result()
                print(f"Task completed with result: {result}")
            except Exception as exc:
                print(f"Task generated an exception: {exc}")


find_factorial_by_thread_pool()


# Завдання 2
# Створіть три функції, одна з яких читає файл на диску із заданим ім'ям та перевіряє наявність рядка «Wow!».
# Якщо файлу немає, то засипає на 5 секунд, а потім знову продовжує пошук по файлу.
# Якщо файл є, то відкриває його і шукає рядок «Wow!».
# За наявності цього рядка закриває файл і генерує подію,
# а інша функція чекає на цю подію і у разі її виникнення виконує видалення цього файлу.
# Якщо рядки «Wow!» не було знайдено у файлі, то засипати на 5 секунд.
# Створіть файл руками та перевірте виконання програми.


def read_file(file_path, str_name):

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if str_name in line:
                    print("String found")
                    thread12.start()
                else:
                    time.sleep(5)
                    print("No string found")
    else:
        time.sleep(5)
        print("No file found")


def rem_file(file_path):

    os.remove(file_path)
    print("File removed")


thread11 = threading.Thread(target=read_file, args=("test.txt", "Wow!"))
thread12 = threading.Thread(target=rem_file, args=("test.txt",))

thread11.start()
