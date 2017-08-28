import re

# ^[0-9]*$
# ^[0-9]{2}/[0-9]{2}/[0-9]{2,4}$
# \d{1,3}(?:\s[a-zA-Z]+)+,(?:\s[a-zA-Z]+)+
# ([0-9])\1

# text = open("test-file.txt")
# print(text.read())

# with open("test-file.txt", "r") as text:
# 	policy = re.search(r'Policy Number:\s+[0-9]+', text.read())
# 	print(policy.group())
# text.close()

# with open("test-file.txt", "r") as text:
# 	claim = re.search(r'Claim Number:\s+[a-zA-Z]+[-]+[0-9]+', text.read())
# 	print(claim.group())
# text.close()



# with open('test-file.txt', 'r') as file:
# 	data = file.read()
# 	match = re.findall(r'[A-Z]{2}-\d{6}:[0-9][A-Z]', data)
# 	print(match)



with open('test-file.txt', 'r') as file:
	data = file.readlines()
	print(data)
	for i,d in enumerate(data):
		match = re.search(r'^X$', d)
		print(i,match)
		