-- First name and last name of of students born after the year 2000
SELECT FirstName, LastName
FROM Student
WHERE YearOfBirth > 2000;

-- All information relating to teachers
SELECT *
FROM Teacher;

-- All information relating to teachers and courses
SELECT *
FROM Teacher 
INNER JOIN Course ON TeacherID = CourseTeacher;

-- Firs name and last name of the students with their courses and their teachers
SELECT Student.FirstName, Student.LastName, Course.CourseName, Teacher.LastName
FROM Student 
	INNER JOIN Exam ON Student.StudentID = Exam.StudentID
	INNER JOIN Course ON Exam.CourseID = Course.CourseID
	INNER JOIN Teacher ON Course.CourseTeacher = Teacher.TeacherID
WHERE exam.Evaluation > 25;
