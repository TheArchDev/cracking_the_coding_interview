## Initial solution
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

# Improvement to solution, after checking first book solution
# Taking base/initial case out of the for loop
'''SPACE COMPLEXITY: O(1)?? I use 4 or 5 variables through the process, all of which are integers or strings...'''
'''TIME COMPLEXITY: Runtime is O(p+k^2) where p: size of original string, k: number of character sequences.
'''
'''String concatenation operates in O(n^2).
(PROOF/DISCUSSION Where you're concatenating a list of n strings, one at a time, into a single end string. Assume each is length x. Then at each concatenation, a new copy of the temp-string is created and the temp-string and the string-addition are copied over character by character to become the new temp-string. First time, x characters, second time, 2x characters ... etc... final time, nx characters are copied over. O(x + 2x + ... + nx) reduces to O(xn^2)
	This is largely due to fact strings are immutable, and so a new representation must be created)'''
'''NB how no sequences greater than 1 would be the worst case, as that would mean the else branch would fire every time, and the if branch has fewer processes to execute'''

# string = raw_input()
# temp = string[0]
# count = 1
# output = ''

# for x in range(1,len(string)):
# 	if string[x] == temp:
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

#Another solution after hearing about StringBuffer in Java
#Attempted to use Python join instead
''' SPACE COMPLEXITY: O(n)?? Due to the array having n elements, then 3/4 other integer or string variables'''
'''TIME COMPLEXITY ''.join(seq) is a O(n) process, vs when using += possibly being O(n^2)'''

string = raw_input()
temp = string[0]
count = 1
output = [temp]

for x in xrange(1,len(string)):
	if string[x] == temp:
		count += 1
	else:
		output.append(str(count))
		temp = string[x]
		output.append(temp)
		count = 1

output.append(str(count))

if len(output) < len(string):
	print ''.join(output)
else:
	print string


#Slight variation with regard to order and handling of edge cases

# string = raw_input()
# temp = string[0]
# count = 1
# output = []

# for x in xrange(1,len(string)):
# 	if string[x] == temp:
# 		count += 1
# 	else:
# 		output.append(temp)
# 		output.append(str(count))
# 		temp = string[x]
# 		count = 1

# output.append(temp)
# output.append(str(count))

# if len(output) < len(string):
# 	print ''.join(output)
# else:
# 	print string