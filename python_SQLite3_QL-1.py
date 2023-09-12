import sqlite3

university_db = sqlite3.connect("university.db")

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
