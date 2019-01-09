class School(object):
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        self.students.update({name:grade})

    def roster(self):
        return [names
                for grades in range(max(self.students.values()) + 1)
                for names in self.grade(grades)]

    def grade(self, grade_number):
        return sorted([name
                       for name, grade in self.students.items()
                       if grade == grade_number])
