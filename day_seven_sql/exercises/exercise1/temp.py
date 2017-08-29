import sqlite3

db = 'nameOfDatabase.db'

conn = sqlite3.connect(db)

c = conn.cursor()

conn.execute('DROP TABLE name')


c.execute('''
		CREATE TABLE name(
			id Integer Primary Key Autoincrement,
			fname Text,
			lname Text
		)
	''')

conn.commit()


c.execute('''

	INSERT INTO name (fname,lname) VALUES("Art", "Yudin")

	''')

conn.commit()

'''
	SELECT SUM(salary) FROM employee_salary_table;


'''











