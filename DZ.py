import random

classroom_size = 30

def generate_random_students():
    names = ['Алексей', 'Виктор', 'Дмитрий', 'Иван', 'Мария']
    students = []
    for name in names:
        students.append(name)
    while len(students) < classroom_size:
        students.extend(names)
    return students

def choose_random_student():
    return random.choice(generate_random_students())

for _ in range(5):
    print(choose_random_student())
