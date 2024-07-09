/*
Alberto Ferrari
Introduzione all'informatica con Python
*/
INSERT INTO Teacher (TeacherID, LastName, FirstName)
VALUES 	(100, 'Lovelace', 'Ada'),
		(201, 'Turing', 'Alan'),
		(202, 'van Rossum', 'Guido');

INSERT INTO Student (StudentID, LastName, FirstName, YearOfBirth)
VALUES 	(12543, 'Chapman', 'Graham Arthur', 1998),
		(12544, 'Cleese', 'John Marwood', 2001),
		(12001, 'Gilliam', 'Terry', 2000),
		(12006, 'Idle', 'Eric', 2000),
		(12123, 'Jones', 'Terry', 1999),
		(12011, 'Palin', 'Michael', 2002);

INSERT INTO Course (CourseID, CourseName, CourseTeacher)
VALUES	('NTH', 'Number theory', 100),
		('ADS', 'Algorithms and Data Structures', 202),
		('SDE', 'Software Development', 202),
		('A_I', 'Artificial Intelligence', 201);
        
INSERT INTO Exam (Session, CourseID, Evaluation, StudentID)
VALUES	('2023-06-27','ADS',28,12123),
		('2023-06-27','ADS',30,12001),
		('2024-02-09','SDE',30,12006),
		('2024-02-10','A_I',18,12011);
