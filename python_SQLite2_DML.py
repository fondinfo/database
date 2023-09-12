import sqlite3

university_db = sqlite3.connect("university.db")

university_cursor = university_db.cursor()

# Teacher

sql = "INSERT INTO Teacher (TeacherID, LastName, FirstName) VALUES (?, ?, ?)"
val = [
	(100, 'Lovelace', 'Ada'),
	(201, 'Turing', 'Alan'),
	(202, 'van Rossum', 'Guido')
]

university_cursor.executemany(sql, val)

university_db.commit()

# Student 

sql = "INSERT INTO Student (StudentID, LastName, FirstName, YearOfBirth) VALUES (?, ?, ?, ?)"
val = [
		(12543, 'Chapman', 'Graham Arthur', 1998),
		(12544, 'Cleese', 'John Marwood', 2001),
		(12001, 'Gilliam', 'Terry', 2000),
		(12006, 'Idle', 'Eric', 2000),
		(12123, 'Jones', 'Terry', 1999),
		(12011, 'Palin', 'Michael', 2002)
]

university_cursor.executemany(sql, val)

university_db.commit()

# Course

sql = "INSERT INTO Course (CourseID, CourseName, CourseTeacher) VALUES (?, ?, ?)"
val = [
	('NTH', 'Number theory', 100),
	('ADS', 'Algorithms and Data Structures', 202),
	('SDE', 'Software Development', 202),
	('A_I', 'Artificial Intelligence', 201)
]

university_cursor.executemany(sql, val)

university_db.commit()

# Exam

sql = "INSERT INTO Exam (Session, CourseID, Evaluation, StudentID) VALUES (?, ?, ?, ?)"
val = [
('2023-06-27','ADS',28,12123),
		('2023-06-27','ADS',30,12001),
		('2024-02-09','SDE',30,12006),
		('2024-02-10','A_I',18,12011)
]

university_cursor.executemany(sql, val)

university_db.commit()


