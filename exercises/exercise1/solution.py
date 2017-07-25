import sqlite3


# EXCERCISE 1
db = "students.db"

conn = sqlite3.connect(db)

c = conn.cursor()


# IF TABLE ALREADY EXISTS
conn.execute('DROP TABLE student_info')
conn.commit()

c.execute('''
		CREATE TABLE student_info (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			first_name TEXT,
			last_name TEXT,
			age INTEGER,
			homeroom TEXT
		)

	''')

conn.commit()

# EXERCISE 1 END

# EXERCISE 2
fnames = ["Bob", "John", "Sally", "Eric", "Kyle", "Stan", "Chris"]
lnames = ["Bobby", "Johnson", "Turner", "Cartman", "Broflowski", "Marsh", "Griffin"]
ages = [19,16,17,16,16,19,18]
homerooms = ["Beetle", "Grasshopper","Beetle", "Grasshopper","Mantis", "Grasshopper","Mantis"]

for index in range(len(fnames)):
	c.execute('''
		INSERT INTO student_info(first_name,last_name,age,homeroom) VALUES(?,?,?,?)

		''',(fnames[index], lnames[index], ages[index], homerooms[index])
		)

conn.commit()


# EXERCISE 2 END


# EXERCISE 3


# 1.
query = "SELECT * FROM student_info"
result = c.execute(query).fetchall()
print(result)
# 2.
query = "SELECT * from student_info WHERE homeroom = 'Grasshopper'"
result = c.execute(query).fetchall()
print(result)
# 3.
query = "SELECT * from student_info WHERE age = 16"
result = c.execute(query).fetchall()
print(result)
# 4.
query = "SELECT * from student_info WHERE age > 16"
result = c.execute(query).fetchall()
print(result)
# 5.
query = "SELECT age from student_info WHERE homeroom = 'Mantis'"
result = c.execute(query).fetchall()
print(result)
# 6.
query = "SELECT DISTINCT homeroom from student_info WHERE age = 16"
result = c.execute(query).fetchall()
print(result)

# EXERCISE 3 END

