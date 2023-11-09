def grades_average(grades):
    grades_count = 0
    grades_sum = 0
    for course in grades:
        grades_count += len(grades[course])
        grades_sum += sum(grades[course])
    return round(grades_sum / grades_count, 1)


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.grades_average_homework = []

    def rate_hw_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def grades_average(self):
        grades_count = 0
        grades_sum = 0
        for grade in self.grades_student:
            grades_count += len(self.grades_student[grade])
            grades_sum += sum(self.grades_student[grade])
        return grades_sum / grades_count

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {grades_average(self.grades_student)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}\n")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_lecturer = {}


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_lecturer = {}
        self.grades_average_lecture = []

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {grades_average(self.grades_lecturer)}\n")


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n")


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

awesome_lecturer = Lecturer('Another', 'Lecturer')
awesome_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw_student(best_student, 'Python', 8)
cool_mentor.rate_hw_student(best_student, 'Python', 7)
cool_mentor.rate_hw_student(best_student, 'Python', 9)
cool_mentor.rate_hw_student(best_student, 'Git', 10)

best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 8)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 9)
best_student.rate_hw_lecturer(awesome_lecturer, 'Python', 10)

print('ok')
print(cool_mentor)
print(awesome_lecturer)
print(best_student)

