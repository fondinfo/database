import mysql.connector

university_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="---",
  database="university"
)

university_cursor = university_db.cursor()

uni_sql = '''
CREATE TABLE Teacher (
	TeacherID int NOT NULL,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	PRIMARY KEY (TeacherID)
)
'''

university_cursor.execute(uni_sql)

uni_sql = '''
CREATE TABLE Course (
	CourseID char(3) NOT NULL,
	CourseName varchar(255) NOT NULL,
	CourseTeacher int,
	PRIMARY KEY (CourseID),
	FOREIGN KEY (CourseTeacher) REFERENCES Teacher(TeacherID)
)
'''

university_cursor.execute(uni_sql)

uni_sql = '''    
CREATE TABLE Student (
	StudentID int NOT NULL,
	LastName varchar(255) NOT NULL,
	FirstName varchar(255),
	YearOfBirth INT NOT NULL,
	PRIMARY KEY (StudentID)
)
'''

university_cursor.execute(uni_sql)


uni_sql = '''
CREATE TABLE Exam (
	ExamID int NOT NULL AUTO_INCREMENT,
	Session Date,
	CourseID char(3) NOT NULL,
	Evaluation int,
	StudentID int NOT NULL,
	PRIMARY KEY (ExamID),
	FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
	FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
)
'''

university_cursor.execute(uni_sql)
