#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

university_db = myclient["university"]

university_col = university_db["Teacher"]

print('university_col.find()',type(university_col.find()))

for t in university_col.find():
  print(t,type(t))
