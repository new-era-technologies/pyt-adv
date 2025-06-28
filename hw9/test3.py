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

        self.student1 = Student('Aa', 'Aaa', 17, 4.0)
        self.student2 = Student('Bb', 'Bbb', 18, 4.1)
        self.student2 = Student('Cc', 'Ccc', 19, 3.7)
        self.student2 = Student('Dd', 'Ddd', 20, 2.1)
        self.student2 = Student('Ee', 'Eee', 21, 5.0)

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

            self.assertNotEqual(student.name, student.surname, "Name and surname cant be same")

            self.assertGreater(5.01, student.average_grade, "Average_grade cant be greater than 5")
            self.assertGreater(150, student.age, "Age cant be greater than 150")

            self.assertIsInstance(student, Student, "student is an instance of class Student")

            self.assertTrue(student.name.istitle(), "Name can be start from upper letter")
            self.assertTrue(student.surname.istitle(), "Surname can be start from upper letter")

unittest.main()