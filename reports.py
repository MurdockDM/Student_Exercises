import sqlite3
from exercise import Exercise
from cohort import Cohort
from student import Student
from instructor import Instructor


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/dustinmurdock/workspace/python/Student_Exercises/studentexercises.db"

    def all_students(self):
        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Cohort_Name
            FROM Student s
            JOIN Cohort c ON s.Cohort_Id = c.Id
            """)

            all_students = db_cursor.fetchall()

            print('\nAll students')
            [print(s) for s in all_students]

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
            e.NAME,
            e.exercise_language
            FROM Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            print('\nAll exercises')
            [print(s) for s in all_exercises]

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Id,
            c.Cohort_Name
            FROM Cohort c """)

            all_cohorts = db_cursor.fetchall()
            print('\nAll Cohorts')
            [print(s) for s in all_cohorts]

    def all_javascript_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
            e.NAME,
            e.exercise_language
            FROM Exercise e
            WHERE e.exercise_language LIKE 'Javascript'
            """)

            all_exercises = db_cursor.fetchall()

            print('\nJavascript only exercises')
            [print(s) for s in all_exercises]

    def all_python_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT e.Id,
            e.NAME,
            e.exercise_language
            FROM Exercise e
            WHERE e.exercise_language LIKE 'Python'
            """)

            all_exercises = db_cursor.fetchall()

            [print(s) for s in all_exercises]

    def all_students_with_cohort(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2],
                                                           row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack_Handle,
                s.Cohort_Id,
                c.Cohort_Name
            from Student s
            join Cohort c on s.Cohort_Id = c.Id
            order by s.Cohort_Id
            """)

            all_students_with_cohort = db_cursor.fetchall()

            print("\nAll students by Cohort")
            [print(s) for s in all_students_with_cohort]

    def all_instructors_with_cohort(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[6], row[4])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack_Handle,
                i.Cohort_Id,
                i.Specialty,
                c.Cohort_Name
            from Instructor i
            join Cohort c on i.Cohort_Id = c.Id
            order by i.Cohort_Id
            """)

            all_instructors_with_cohort = db_cursor.fetchall()

            print("\nAll instructors by Cohort")
            [print(s) for s in all_instructors_with_cohort]

    def all_exercises_with_students(self):

        exercises = dict()


        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.First_Name,
                    s.Last_Name
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')

    def all_students_working_exercises(self):

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    s.Id,
                    s.First_Name,
                    s.Last_Name,
                    e.Id,
                    e.NAME
                FROM Student s
                JOIN StudentExercise se ON se.StudentId = s.Id
                JOIN Exercise e ON e.Id = se.ExerciseId
            """)                            

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            for student_name, exercises in students.items():
                print(f'\n\n{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')


    def exercises_assigned_by_instructor(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute(""" 
                SELECT
                    i.Id,
                    i.First_Name,
                    i.Last_Name,
                    e.Id,
                    e.NAME
                FROM Instructor i
                JOIN StudentExercise se ON se.InstructorId = i.Id
                JOIN Exercise e ON e.Id = se.ExerciseId    """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)

            for instructor_name, exercises in instructors.items():
                print(f'\n\n{instructor_name} has assigned:')
                for exercise in exercises:                                            
                    print(f"\t* {exercise}")


    def exercises_being_worked_on(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.Id,
                    e.NAME,
                    s.Id,
                    s.First_Name,
                    s.Last_Name
                FROM Exercise e
                JOIN StudentExercise se ON se.StudentId = e.Id
                JOIN Student s ON s.Id = se.ExerciseId
            """)                            

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                exercise_id = row[0]
                exercise_name = row[1]

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            for exercise_name, students in exercises.items():
                print(f'\n\n{exercise_name} is being worked on by:')
                for student in students:
                    print(f'\t* {student}')

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_exercises()
reports.all_python_exercises()
reports.all_students_with_cohort()
reports.all_instructors_with_cohort()
reports.all_exercises_with_students()
reports.all_students_working_exercises()
reports.exercises_assigned_by_instructor()
reports.exercises_being_worked_on()