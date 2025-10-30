class Student():
    def __init__(self, nome, age, gpa, enrolled):
        self.nome = nome
        self.age = age
        self.gpa = gpa
        self.enrolled = enrolled

    def display_info(self):
        print('The student {} GPA is {}.'.format(self.nome, self.gpa))

joao = Student('João', 25, 4.5, True)

joao.display_info()
