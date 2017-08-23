

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

	def __len__(self):
		return self.age * 8

	def __eq__(self,pet2):
		return self.age == pet2.age

dog = Pet("Sparky", 6, "dog")
dog2 = Pet("Bruno", 6, "dog")
cat = Pet("Biggles", 4, "cat")

dog.introduce()
print(dog.next_year())

print(dog + cat)

print(len(dog))

print(dog == dog2)

