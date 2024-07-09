#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print('myclient',type(myclient))

university_db = myclient["university"]
print('university_db',type(university_db))

university_col = university_db["Student"]
print('university_col',type(university_col))

student_data = { "LastName": "Idel", "FirstName": "Eric", "YearOfBirth": 2000 }
print('student_data',type(student_data))

s = university_col.insert_one(student_data)
print('s',type(s))
help(type(s))

print(s.inserted_id)
print('s.inserted_id',type(s.inserted_id))
