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
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2],
            row[3], row[6], row[4])
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


reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_javascript_exercises()
reports.all_python_exercises()
reports.all_students_with_cohort()
reports.all_instructors_with_cohort()