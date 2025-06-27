# Завдання 1
# Створити функцію, яка допоможе порахувати швидкість автомобіля. 
# Набір даних, який використовується для розрахунку: 
# * довжина шляху;
# * тривалість шляху.
# Створити 5-7 тестів використовуючи оператор assert. 


def calculate_speed(d: int, t: int):
    s = d / t

    assert d > 0, "distance must be not null and not negative"
    assert t > 0, "time must be not null and not negative"

    return s

def test_calculating():
      assert calculate_speed(100, 2) == 50, "asserts that 100/2 equals 50"


print(calculate_speed(5, 3))