from person import Person

class Student(Person):

    def __init__(self, first_name, last_name, slack_handle, cohort_name):
        super().__init__(first_name, last_name, slack_handle, cohort_name)
        self.__current_exercises = list()

    def new_exercise(self, exercise):
        self.__current_exercises.append(exercise)    