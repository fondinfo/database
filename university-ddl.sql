CREATE DATABASE University;
USE University;

CREATE TABLE Teacher (
	TeacherID int NOT NULL,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	PRIMARY KEY (TeacherID)
);
    
CREATE TABLE Course (
	CourseID char(3) NOT NULL,
	CourseName varchar(255) NOT NULL,
	CourseTeacher int,
	PRIMARY KEY (CourseID),
	FOREIGN KEY (CourseTeacher) REFERENCES Teacher(TeacherID)
);
    
CREATE TABLE Student (
	StudentID int NOT NULL,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	YearOfBirth INT NOT NULL,
	PRIMARY KEY (StudentID),
	CHECK (YearOfBirth < 2023)
);

CREATE TABLE Exam (
	ExamID int NOT NULL AUTO_INCREMENT,
	Session Date,
	CourseID char(3) NOT NULL,
	Evaluation int,
	StudentID int NOT NULL,
	PRIMARY KEY (ExamID),
	FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
	FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);
