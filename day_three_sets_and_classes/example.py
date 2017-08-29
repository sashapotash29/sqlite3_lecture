

class Person:

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return "class: Person Class, Name is {}".format(self.name)

	def __add__(self,person2):
		return "My new name is: {}{}".format(self.name[0:len(self.name)//2], person2.name[0:len(self.name)//2])



	def introduce(self, index = 0):

		print("Hi my name is {}".format(self.name))

	def next_year(self):
		return self.age + 1



# class newList:

# 	def __init__(self, list1):
# 		self.list1 = list1

# 	def pop(self, index = 0):
# 		if index == 0:
# 			value_to_return = self.list1[0]
# 			self.list1 = self.list1[1:len(self.list1)]
# 		else:
# 			value_to_return = self.list1[index]
# 			self.list1 = self.list1[0:index] + self.list1[index+1:len(self.list1)]

# 		return value_to_return




# nl = newList("apple")

# print(nl)
# print(nl.pop())
# print(nl.list1)



person1 = Person("Tom", 24)
person2 = Person("Bob", 32)
person2 = person1

person1.introduce()
person2.introduce()


print(person1 + person2)


