from cohort import Cohort
from exercise import Exercise
from student import Student
from instructor import Instructor


exercise1 = Exercise("exercise_1", "Javascript")
exercise2 = Exercise("exercise_2", "Javascript")
exercise3 = Exercise("exercise_3", "Python")
exercise4 = Exercise("exercise_4", "Python")
exercise5 = Exercise("exercise_5", "Python")
exercise6 = Exercise("exercise_6", "Python")

cohort37 = Cohort("Cohort 37")
cohort38 = Cohort("Cohort 38")
cohort39 = Cohort("Cohort 39")

student1 = Student("Robert", "Robertson", "robrob", cohort38)
student2 = Student("Janice", "Haymai", "JHay", cohort38)
student3 = Student("John", "Specter", "ghosty", cohort38)
student4 = Student("Mary", "Thompkins", "MThompkins", cohort38)

instructor1 = Instructor("Andy", "Collins", "Andy Collins", cohort38, "quotable quotes")
instructor2 = Instructor("Jisie", "David", "Jisie David", cohort38, "great sense of humor")
instructor3 = Instructor("Kristen", "Norris", "Kristen Norris", cohort38, "ability to break the code down")

students = [student1, student2, student3, student4]

for student in students:
    instructor2.give_student_exercise(student, exercise1)
    instructor2.give_student_exercise(student, exercise5)   

