#!/usr/bin/env python3
"""
@author  Alberto Ferrari - https://albertoferrari.github.io/
@license This software is free - https://opensource.org/license/mit
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

university_db = myclient["university"]

university_col = university_db["Teacher"]
  
university_query = { "FirstName": "Alan" }

university_res = university_col.find(university_query)

for t in university_res:
  print(t)
