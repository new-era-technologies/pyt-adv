# Завдання 3
# Створити клас, у який дозволяє зберігати дані про студента:
# - ім'я;
# - прізвище;
# - вік;
# - середній бал.
# Створіть список з 10 студентів-інстансів даного класу 
# та протестуйте валідність даних використовуючи пакет unittest.


import unittest


class Student:

    def __init__(self, name: str, surname: str, age: int, average_grade: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def __repr__(self):
        info = f'name: {self.name} \nsurname: {self.surname} \nage: {self.age} \naverage_grade: {self.average_grade}'
        return info



class StudentInfo:
    def __init__(self):
        self.students = []

        self.student1 = Student(None, 'Aaa', 17, 4.0)
        self.student2 = Student('Bb', 'Bbb', 18, 4.1)

        self.students.append(self.student1)
        self.students.append(self.student2)

    def __repr__(self):
        return self.students

    def get_all_students_info(self):
        return self.students


class TestStudent(unittest.TestCase):

    # @unittest.skip("demonstrating skipping")
    def test_student_info_not_none(self):
        student_instance_info = StudentInfo()
        students = student_instance_info.get_all_students_info()
        for student in students:
            self.assertIsNotNone(student.name, "Name cant be None")
            self.assertIsNotNone(student.surname, "Surname cant be None")
            self.assertIsNotNone(student.age, "Age cant be None")
            self.assertIsNotNone(student.average_grade, "Grade cant be None")
    


unittest.main()