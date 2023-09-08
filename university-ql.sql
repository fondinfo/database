SELECT FirstName, LastName
FROM Student
WHERE YearOfBirth > 2000;

SELECT *
FROM Teacher;

SELECT *
FROM Teacher 
INNER JOIN Course ON TeacherID = CourseTeacher;

SELECT Student.FirstName, Student.LastName, Course.CourseName, Teacher.LastName
FROM Student 
	INNER JOIN Exam ON Student.StudentID = Exam.StudentID
	INNER JOIN Course ON Exam.CourseID = Course.CourseID
	INNER JOIN Teacher ON Course.CourseTeacher = Teacher.TeacherID
WHERE exam.Evaluation > 25;
