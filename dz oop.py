class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_2:
                lecturer.grades_2[course] += [grade]
            else:
                lecturer.grades_2[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_2 = {}

    def average_rating(self):
        self.average = round(sum(sum(self.grades_2.values(), [])) / len(sum(self.grades_2.values(), [])), 1)
        return self.average

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


gon = Student("Gon", "Gudro", "man")
inga = Student("Inga", "Persson", "woman")

endry = Lecturer("Endry", "Coulman")
ron = Lecturer("Ron", "Burk")

roy = Reviewer("Roy", "Matius")
roman = Reviewer("Roman", "Yosi")

gon.courses_in_progress += ['Python']
gon.finished_courses += ['Java']
inga.courses_in_progress += ['C']
inga.courses_in_progress += ['Python']
inga.finished_courses += ['Git']

endry.courses_attached += ['C', 'Java', 'Python']
ron.courses_attached += ['Python', 'Git']

roy.courses_attached += ['Python', 'Java']
roman.courses_attached += ['C', 'Git']

gon.rate_l(ron, 'Python', 8)
gon.rate_l(ron, 'Python', 9)
gon.rate_l(ron, 'Python', 6)
inga.rate_l(ron, 'Python', 7)
inga.rate_l(ron, 'Python', 10)
inga.rate_l(ron, 'Python', 8)
inga.rate_l(endry, 'C', 10)
inga.rate_l(endry, 'C', 8)
inga.rate_l(endry, 'C', 10)
inga.rate_l(endry, 'Python', 6)
inga.rate_l(endry, 'Python', 8)
inga.rate_l(endry, 'Python', 9)

roy.rate_hw(gon, 'Python', 8)
roy.rate_hw(gon, 'Python', 6)
roy.rate_hw(gon, 'Python', 4)
roy.rate_hw(inga, 'Python', 8)
roy.rate_hw(inga, 'Python', 9)
roy.rate_hw(inga, 'Python', 10)

gon.average_grade()
inga.average_grade()
print(gon < inga)
print(gon)
print(inga)

endry.average_rating()
ron.average_rating()
print(endry < ron)
print(endry)
print(ron)

print(roy)
print(roman)

students_list = [gon, inga]


def grade_av(students_list, course):
    sum = 0
    count = 0
    for x in students_list:
        for y in x.grades[course]:
            sum += y
            count += 1
    return round(sum/count, 1)

lecturers_list = [endry, ron]


def rating_al(lecturers_list, course):
    sum = 0
    count = 0
    for x in lecturers_list:
        for y in x.grades_2[course]:
            sum += y
            count += 1
    return round(sum/count, 1)

print(grade_av(students_list, 'Python'))
print(rating_al(lecturers_list, 'Python'))


