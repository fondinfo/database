import sqlite3

university_db = sqlite3.connect("university.db")

university_cursor = university_db.cursor()

# First name and last name of of students born after the year 2000
sql = '''
SELECT FirstName, LastName
FROM Student
WHERE YearOfBirth > 2000;
'''

university_cursor.execute(sql)

university_result = university_cursor.fetchall()

# university_result is a list of tuple

for res in university_result:
	print(res)


# All information relating to teachers and courses
sql = '''
SELECT *
FROM Teacher 
INNER JOIN Course ON TeacherID = CourseTeacher;
'''

university_cursor.execute(sql)
university_result = university_cursor.fetchall()
for res in university_result:
	print(res)

# Firs name and last name of the students with their courses and their teachers
sql = '''
SELECT Student.FirstName, Student.LastName, Course.CourseName, Teacher.LastName
FROM Student 
	INNER JOIN Exam ON Student.StudentID = Exam.StudentID
	INNER JOIN Course ON Exam.CourseID = Course.CourseID
	INNER JOIN Teacher ON Course.CourseTeacher = Teacher.TeacherID
WHERE exam.Evaluation > 25;
'''

university_cursor.execute(sql)
university_result = university_cursor.fetchall()
for res in university_result:
	print(res)
