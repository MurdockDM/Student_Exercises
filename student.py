from person import Person

class Student(Person):

    def __init__(self, first_name, last_name, slack_handle, cohort_name):
        super().__init__(first_name, last_name, slack_handle, cohort_name)
        self.__current_exercises = list()

    def new_exercise(self, exercise):
        self.__current_exercises.append(exercise)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort_name}'        