from person import Person

class Instructor(Person):
    def __init__(self, first_name, last_name, slack_handle, cohort_name, specialty):
        super().__init__(first_name, last_name, slack_handle, cohort_name)
        self.specialty = specialty


    def give_student_exercise(self, student, exercise ):
        student.new_exercise(exercise)