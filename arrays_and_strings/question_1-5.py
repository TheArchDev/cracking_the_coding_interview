##Initial solution
# string = raw_input()
# temp = ''
# count = 0
# output = ''

# for x in range(len(string)):
# 	if x == 0:
# 		temp = string[x]
# 		count += 1
# 	elif string[x] == temp:
# 		count += 1
# 	else:
# 		output += temp + str(count)
# 		temp = string[x]
# 		count = 1

# output += temp + str(count)

# if len(output) < len(string):
# 	print output
# else:
# 	print string

#Improvement to solution, after checking first book solution
#Taking base/initial case out of the for loop

string = raw_input()
temp = string[0]
count = 1
output = ''

for x in range(1,len(string)):
	if string[x] == temp:
		count += 1
	else:
		output += temp + str(count)
		temp = string[x]
		count = 1

output += temp + str(count)

if len(output) < len(string):
	print output
else:
	print string
