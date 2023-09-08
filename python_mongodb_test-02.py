import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

university_db = myclient["university"]

university_col = university_db["Student"]

student_data = { "LastName": "Idel", "FirstName": "Eric", "YearOfBirth": 2000 }

s = university_col.insert_one(student_data)

