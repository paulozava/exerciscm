class Garden(object):
    def __init__(self, diagram, students=None):
        STD_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

        self.diagram = diagram.split()
        self.students = sorted(students) if students else STD_STUDENTS
        self.abv_to_fullname = {'G': 'Grass', 'C': 'Clover', 'R':'Radishes', 'V':'Violets'}

    def plants(self, student):
        start_pos = 2 *self.students.index(student)
        end_pos = start_pos + 2
        return [self.abv_to_fullname[item]
                for line in self.diagram
                for item in line[start_pos:end_pos]
               ]
