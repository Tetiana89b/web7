from datetime import datetime
from random import randint

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from baza_2 import Base, Grade, Group, Student, Subject, Teacher

# Створення бази даних та підключення до неї
engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
fake = Faker()

# Генерація студентів
students_count = randint(30, 50)
for _ in range(students_count):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = randint(1, 3)  # Випадково обираємо групу
    student = Student(first_name=first_name,
                      last_name=last_name, group_id=group_id)
    session.add(student)

# Генерація груп
groups = ["Group A", "Group B", "Group C"]
for group_name in groups:
    group = Group(name=group_name)
    session.add(group)

# Генерація викладачів
teachers_count = randint(3, 5)
for _ in range(teachers_count):
    first_name = fake.first_name()
    last_name = fake.last_name()
    teacher = Teacher(first_name=first_name, last_name=last_name)
    session.add(teacher)

# Генерація предметів
subjects_count = randint(5, 8)
for _ in range(subjects_count):
    name = fake.job()
    teacher_id = randint(1, teachers_count)  # Випадково обираємо викладача
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)

# Генерація оцінок для кожного студента з усіх предметів
students = session.query(Student).all()
subjects = session.query(Subject).all()
for student in students:
    for subject in subjects:
        grades_count = randint(1, 20)
        for _ in range(grades_count):
            grade = randint(1, 100)
            date = fake.date_between(start_date='-1y', end_date='today')
            grade_record = Grade(student_id=student.id,
                                 subject_id=subject.id, grade=grade, date=date)
            session.add(grade_record)

# Збереження змін до бази даних
session.commit()

# Закриття сесії
session.close()
