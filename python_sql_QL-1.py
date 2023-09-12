import mysql.connector

university_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="----",
  database="university"
)

university_cursor = university_db.cursor()

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
