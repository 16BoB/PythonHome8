# 2)Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки
from random import choice
from random import randint

class Student:
    def __init__(self, name, group, progress) -> None:
        self.name = name
        self.group = group
        self.progress = progress

    def __str__(self) -> str:
        return f'Name: {self.name}, Group: {self.group}, Progress: {self.progress}'

students = []
n = 10
names = ['Vasya', 'Kolya', 'Petya', 'Sasha', 'Masha', 'Kirill', 'Artem', 'Nikita']
for i in range(n):
    students.append(Student(choice(names), str(randint(1,22)), randint(1, 5)))

print('PRINT ALL STUDENTS')
for i in students:
    print(i)

students.sort(key=lambda x: x.name)
print('SORTED BY NAME')
for i in students:
    print(i)

print('PRINT LOW PROGRESS')
for i in students:
    if i.progress <= 3:
        print(i)