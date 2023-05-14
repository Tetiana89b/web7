from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from baza_2 import Grade, Group, Student, Subject, Teacher


def select_1(session):
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    result = session.query(Student).\
        join(Grade, Student.id == Grade.student_id).\
        group_by(Student.id).\
        order_by(func.avg(Grade.grade).desc()).\
        limit(5).all()
    return result


def select_2(session, subject_id):
    # Знайти студента із найвищим середнім балом з певного предмета
    result = session.query(Student).\
        join(Grade, Student.id == Grade.student_id).\
        filter(Grade.subject_id == subject_id).\
        group_by(Student.id).\
        order_by(func.avg(Grade.grade).desc()).\
        first()
    return result


def select_3(session, subject_id):
    # Знайти середній бал у групах з певного предмета
    result = session.query(func.avg(Grade.grade)).\
        join(Student, Student.id == Grade.student_id).\
        filter(Student.group_id == Group.id).\
        filter(Grade.subject_id == subject_id).\
        group_by(Group.id).all()
    return result


def select_4(session):
    # Знайти середній бал на потоці (по всій таблиці оцінок)
    result = session.query(func.avg(Grade.grade)).scalar()
    return result


def select_5(session, teacher_id):
    # Знайти які курси читає певний викладач
    result = session.query(Subject).\
        filter(Subject.teacher_id == teacher_id).all()
    return result


def select_6(session, group_id):
    # Знайти список студентів у певній групі
    result = session.query(Student).\
        filter(Student.group_id == group_id).all()
    return result


def select_7(session, group_id, subject_id):
    # Знайти оцінки студентів у окремій групі з певного предмета
    result = session.query(Grade).\
        join(Student, Student.id == Grade.student_id).\
        filter(Student.group_id == group_id).\
        filter(Grade.subject_id == subject_id).all()
    return result


def select_8(session, teacher_id):
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    result = session.query(func.avg(Grade.grade)).\
        join(Subject, Subject.id == Grade.subject_id).\
        filter(Subject.teacher_id == teacher_id).scalar()
    return result


def select_9(session, student_id):
    # Знайти список курсів, які відвідує певний студент
    result = session.query(Subject).\
        join(Grade, Subject.id == Grade.subject_id).\
        filter(Grade.student_id == student_id).all()
    return result


def select_10(session, student_id, teacher_id):
    # Список курсів, які певному студенту читає певний викладач
    result = session.query(Subject).\
        join(Grade, Subject.id == Grade.subject_id).\
        filter(Grade.student_id == student_id).\
        filter(Subject.teacher_id == teacher_id).all()
    return result
