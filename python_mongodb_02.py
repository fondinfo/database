import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

university_db = myclient["university"]

university_col = university_db["Teacher"]

teacher_list = [
  { "_id": 100, "LastName": "Lovelace", "FirstName": "Ada"},
  { "_id": 201, "LastName": "Turing", "FirstName": "Alan", "Courses": "Artificial Intelligence"},  
  { "_id": 202, "LastName": "van Rossum", "FirstName": "Guido", 
"Courses": ["Algorithms and Data Structures","Software Development"]}
]

t = university_col.insert_many(teacher_list)

#print list of the _id values of the inserted documents:
print(t.inserted_ids)

