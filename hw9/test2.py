# Завдання 2
# Взяти функцію розрахунку маси тіла з Python Starter українською/Домашнє_завдання 8/Завдання 5. 
# Покрити її 10 тестами, щоб перевірити роботоздатність, 
# використовуючи заздалегідь валідні дані та навпаки(введення текстових даних у поля, від'ємні значення тощо).
# За необхідності взяти її та доопрацювати до максимально стабільного варіанту.
# В процессі тестування використати:
# - оператор assert;
# - pytest;
# -unittest. 

import pytest

# @pytest.fixture
def check_bmi(height: float, weight: int):
    bmi = weight / (height * height)

    if bmi < 18.5:
        print("Low weight")
    elif 18.5 <= bmi <= 24.9:
        print("Normal weight")
    elif 25 <= bmi <= 29.9:
        print("Big weight")
    else:
        print("Very very big weight")
        
    return bmi

# height = input("Enter your height")
# weight = input("Enter your weight")

@pytest.mark.parametrize("height, lower, upper, expected_result", [
    (1.5, 0.5, 2.5, True),  # Number within range
    (0.1, 0.5, 2.5, False), # Number below range
    (3, 0.5, 2.5, False), # Number above range
    (0.5, 0.5, 2.5, True),  # Lower bound included
    (2.5, 0.5, 2.5, True), # Upper bound included
])
def test_height_in_range_parametrized(h, low, up, ex_res):
    res = low <= h <= up
    assert res == ex_res

@pytest.mark.parametrize("weight, lower, upper, expected_result", [
    (70, 2, 250, True),  # Number within range
    (0.1, 2, 250, False), # Number below range
    (270, 250, False), # Number above range
    (2, 2, 250, True),  # Lower bound included
    (250, 2, 250, True), # Upper bound included
])
def test_height_in_range_parametrized(w, low, up, ex_res):
    res = low <= w <= up
    assert res == ex_res


# check_bmi(height, weight)

