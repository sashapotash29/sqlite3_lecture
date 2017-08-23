from ../specialfolder/name_of_file import className

from functionfile import adding, subtracting, measure, x




class Pet:

	def __init__(self, name, age, pet_type):
		self.name = name
		self.age = age
		self.pet_type = pet_type


	def introduce(self):
		print("Hi my name is {} and I am a {}.".format(self.name,self.pet_type))


	def next_year(self):
		next_year = self.age + 1
		return next_year

	def __str__(self):
		return "{} the {}".format(self.name,self.pet_type)

	def __add__(self,pet2):
		return "This is a half {} and half {} montrosity!! It goes by {}".format(self.pet_type,pet2.pet_type, self.name+pet2.name)
		# return self.age + pet2.age

	def __len__(self):
		return self.age * 8

	def __eq__(self,pet2):
		return self.age == pet2.age

	def explain_yourself(self):
		print('''
				So this guy art told me to make a class and it can do some inter


				__iter__ is designed to give you every movie in the movie list one by one. Note that moveis with a nimer

			''')



if __name__ == "__main__":
	dog = Pet("Sparky", 6, "dog")
	dog2 = Pet("Bruno", 6, "dog")
	cat = Pet("Biggles", 4, "cat")

	# dog.introduce()
	# print(dog.next_year())

	# print(dog + cat)

	# print(len(dog))

	# print(dog == dog2)

