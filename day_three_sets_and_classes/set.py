from datetime import datetime
import time
# #  BASIC SETS

# # - Sets are a data structure similar to an array/list.
# # - However, sets allow us to do quicker comparisons between multiple
# # collections of items.
# # Sets only can contain one of any value (no duplicates)


# example = set()

# # ADDING ITEMS TO A SET
# example.add(3)
# example.add(3) # NOTE This line of code will neither add the number 3 to the Set() nor raise an exception.
# example.add(4)
# example.add("string")
# example.add("blue")
# # example.add([1,2,3,4,5]) # NOTE Sets only accept hashable values meaning no lists, dictionaries, and etc.
# # print(example)



# #  REMOVING ITEMS FROM A SET
# example.remove(4)

# # print(example)

# # a Set can also be created by passing a collection of items such as a list and a tuple
example2 = set([5,3,6,"string","red"])
# example3 = set((5,3,6,"string","red"))

# # print(example2)
# # print(example3)

# # # Comparing Sets

# #  Union allows us to compare two sets and return a set with all unique items in both sets
# result = example.union(example2)
# # print(result)

# # Intersection allows us to return all the values that each set has in common.
# result = example.intersection(example3)
# # print(result)











# Without Sets
def unique_items(list1,list2):
	final_list = []
	for count, item in enumerate(list1):
		if count % 10000 == 0:
			print("For Loop", count)
		if item not in final_list:
			final_list.append(item)
	for item in list2:
		if item not in final_list:
			final_list.append(item)

	return final_list

x = [number for number in range(80001)]
y = [number for number in range(5000,80001)]


print("Start Old", datetime.now())
unique_items(x,y)
print("End Old", datetime.now())


# # With Sets
def unique_items(list1,list2):
	set1 = set(list1)
	set2 = set(list2)
	return list(set1.union(set2))

print("Start Old", datetime.now())
unique_items(x,y)
print("End Old", datetime.now())










