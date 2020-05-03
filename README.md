# Tracking Student Exercises: Custom Types

You are going to build a console application that tracks exercises that are assigned to students at Nashville Software School. These are the constraints and requirements for your application.


## Student

You must define a custom type for representing a student in code. A student can only be in one cohort at a time. A student can be working on many exercises at a time.

### Properties

1. First name
1. Last name
1. Slack handle
1. The student's cohort
1. The collection of exercises that the student is currently working on

## Cohort

You must define a type for representing a cohort in code.

1. The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)
1. The collection of students in the cohort.
1. The collection of instructors in the cohort.

## Instructor

You must define a type for representing an instructor in code.

1. First name
1. Last name
1. Slack handle
1. The instructor's cohort
1. The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)
1. A method to assign an exercise to a student

## Exercise

You must define a type for representing an exercise in code. An exercise can be assigned to many students.

1. Name of exercise
1. Language of exercise (JavaScript, Python, CSharp, etc.)

## Objective

The learning objective of this exercise is to practice creating instances of custom types that you defined with `class`, establishing the relationships between them, and practicing basic data structures in Python.

## Entity Relationship Diagram

First, build an ERD based on these above requirements using [dbdiagram.io](https://dbdiagram.io).

## Setup

> **Note:** Make sure that each class you define is in its own file.

```sh
mkdir -p ~/workspace/python/StudentExercises && cd $_
touch main.py student.py cohort.py instructor.py exercise.py
code .
```

Once you have defined all of your custom types, go to `main.py`, import the classes you need, and implement the following logic.

1. Create 4, or more, exercises.
1. Create 3, or more, cohorts.
1. Create 4, or more, students and assign them to one of the cohorts.
1. Create 3, or more, instructors and assign them to one of the cohorts.
1. Have each instructor assign 2 exercises to each of the students.

## Challenge

Continuing inside of `main.py` with the instances of the classes you made previously, create the lists below.

##### Example:
If I had a student instance referenced by the variable `ivan`:
```py
students = [ivan]
```


1. Create a list of students. Add all of the student instances to it.
    ```py
    students = list()
    ```
1. Create a list of exercises. Add all of the exercise instances to it.
    ```py
    exercises = list()
    ```

Now, generate a report that displays which students are working on which exercises.

##### Example

```sh
Ivan is working on Kandy Korner, Stocks Report, and Planet List.
```


# Part 2 
# Inheritance for Students and Instructors

Find any common properties and/or behaviors on students and instructors and create a new parent class for both of them to inherit from.

```py
class NSSPerson():
    def __init__(self):
    // What common properties will go here?

```

# Part 3
# Student Exercises Database

## Setup

```sh
cd ~/workspace/python/StudentExercises && cd $_
touch studentexercises.db
tableplus studentexercises.db
```

This will create and open a completely blank SQLite database. In this chapter, you are going to be learning the usage of the following SQL statements.

1. `CREATE TABLE`
1. `INSERT INTO`

## References

* [CREATE TABLE tutorial with examples](http://www.sqlitetutorial.net/sqlite-create-table/)
* [INSERT INTO tutorial with examples](http://www.sqlitetutorial.net/sqlite-insert/)

## Defining your Tables

Read the instructions below and create an ERD of the database before you start creating the tables and inserting the data. Make sure that each table has a primary key column and foreign key constraints for the relationships.
In this part of building your application, you will be creating the database tables and the data that you will be querying in your application logic later.


### Cohort

You must define a table to store data about a cohort. We are giving you the SQL statement for this table, but you have to write the rest of them.

The table must have the following columns.

1. The cohort's name (Evening Cohort 6, Day Cohort 26, etc.)

```sql
CREATE TABLE Cohort (
    Id	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name   TEXT NOT NULL UNIQUE
);
```

### Student

You must define a table to store data about a student. A student can only be in one cohort at a time. A student can be working on many exercises at a time. The table must have the following columns.

1. First name
1. Last name
1. Slack handle
1. The student's cohort

Make sure you create the foreign key constraint as well.

```sql
CREATE TABLE Student (
    ...
    FOREIGN KEY(CohortId) REFERENCES Cohort(Id)
);
```

### Instructor

You must define a table to store data about an instructor. The table must have the following columns.

1. First name
1. Last name
1. Slack handle
1. The instructor's cohort
1. The instructor's specialty (e.g. dad jokes, excitement, dancing, etc.)

### Exercise

You must define a table to store data about an exercise. An exercise can be assigned to many students. The table must have the following columns.

1. Name of exercise
1. Language of exercise (JavaScript, Python, CSharp, etc.)

### Mystery Intersection Table

If you designed your ERD correctly, you should know that there is one more table that you need to define in your database. Create that table now with its primary key and required foreign key constraints.

If you get stuck, or have questions, talk to your instruction team.

## Inserting Sample Data

Use the `INSERT INTO` SQL statement to create...

1. 3 cohorts
1. 5 exercises
1. 3 instructors
1. 7 students _(don't put all students in the same cohort)_
1. Assign 2 exercises to each student

Here's a sample insert statement for an exercise.

```sql
INSERT INTO Exercise (Name, Language)
VALUES ('Kandy Korner', 'JavaScript');
```

# Part 4
# Student Exercise Reports

In this chapter, you are going to use the `sqlite3` package to connect to your `studentexercises.db` database and generate data reports that will output to your terminal.

1. Display all cohorts.
1. Display all exercises.
1. Display all JavaScript exercises.
1. Display all Python exercises.
1. Display all C# exercises.
1. Display all students with cohort name.
1. Display all instructors with cohort name.

# Part 5
## Practice: Student Workload

List the exercises assigned to each student. Display each student name and the exercises s/he has been assigned beneath their name. Use a dictionary to track each student. Remember that the key should be the student id and the value should be the entire student object.

##### Example

```sh
Jessawynne Parker is working on:
    * Stock Report
    * Boy Bands & Vegetables

Tanner Terry is working on:
    * Solar System
    * ChickenMonkey
```

## Practice: Assigned Exercises

List all exercises assigned by each instructor. Display each instructor name and the exercises s/he has assigned beneath their name. Use a dictionary to track each instructor. Remember that the key should be the instructor id and the value should be the entire instructor object.

##### Example

```sh
Joe Shepherd has assigned:
    * Urban Planner

Andy Collins has assigned:
    * Stock Report
    * Bag o Loot
    * Kandy Korner
```

## Practice: Popular Exercises

Output a report in your terminal that lists all students and the exerices each is assigned. Use a dictionary to track each exercise. Remember that the key should be the exercise id and the value should be the entire exercise object.

#### Example

```sh
Overly Excited is being worked on by:
  * Ryan Tanay
  * Meg Ducharme
  * Tanner Terry

Trestlebridge is being worked on by:
  * Steven Holmes
  * Kirren Covey
```