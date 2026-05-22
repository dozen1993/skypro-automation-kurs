class User:
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def Get_first_name(self):
        print('Имя студента:', self.first_name)
    def Get_last_name(self):
        print('Фамилия студента:',self.last_name)
    def Get_full_name(self):
        print('Студент: ', self.first_name, ' ', self.last_name)