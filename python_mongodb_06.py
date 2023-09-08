import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

university_db = myclient["university"]

university_col = university_db["Teacher"]
  
university_query = { "_id": 100 }

teacher_sel = university_col.find_one(university_query)

print(teacher_sel)

if "Courses" not in teacher_sel:
	# first course
	c = "Object Oriented Programming"
else: 
	c = teacher_sel["Courses"]
	if isinstance(c,list):
		# three or more courses
		c.append("Object Oriented Programming")
	else:
		# second course
		c = [c,"Object Oriented Programming"]
	
university_query = { "_id": 100 }
newvalue = { "$set": { "Courses": c } }

university_col.update_one(university_query, newvalue)
