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
'''ASSUMPTIONS: what type of characters? Upper/lower case? Alphanumeric? How large a string?'''
'''SPACE COMPLEXITY: O(n)?? I use 4 or 5 variables through the process, all of which are integers or strings... But think the input string variable scales with with n in space as number of characters grow.'''
'''TIME COMPLEXITY: Runtime is O(p+k^2) where p: size of original string, k: number of character sequences.
'''
'''String concatenation operates in O(n^2).
(PROOF/DISCUSSION Where you're concatenating a list of n strings, one at a time, into a single end string. Assume each is length x. Then at each concatenation, a new copy of the temp-string is created and the temp-string and the string-addition are copied over character by character to become the new temp-string. First time, x characters, second time, 2x characters ... etc... final time, nx characters are copied over. O(x + 2x + ... + nx) reduces to O(xn^2)
	This is largely due to fact strings are immutable, and so a new representation must be created)'''

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
#Then added in compression function to get length of final output BEFORE proceeding with main output-generating function. Think this is only really beneficial if actually can create an array of that specific size afterwards though!
''' SPACE COMPLEXITY: O(n)?? Due to the array having n elements, (then 3/4 other small integer or string variables)'''
'''TIME COMPLEXITY ''.join(seq) is a O(n) process, vs when using += concatenation possibly being O(n^2). In this case, n is now the number of characters AND integers in the final output...'''


def compression(string):
	#handle empty user input
	if string == '':
		return 0

	temp = string[0]
	length = 0
	count = 1
	for x in xrange(1, len(string)):
		if string[x] == temp:
			count += 1
		else:
			#count letter and the length of the number of its consecutive occurrences
			length += 1 + len(str(count))
			temp = string[x]
			count = 1
	length += 1 + len(str(count))
	return length

def main():
	string = raw_input()

	#check if output string would be shorter than input string
	if compression(string) >= len(string):
		return string

	temp = string[0]
	count = 1
	output = [temp]

	for x in xrange(1,len(string)):
		#increase count if repeat letter
		if string[x] == temp:
			count += 1
		#if new letter, add count of previous letter and what the new letter is
		else:
			output.append(str(count))
			temp = string[x]
			output.append(temp)
			count = 1

	#add the count for the final character sequence in the string
	output.append(str(count))
	#output a string from the array
	return ''.join(output)

print main()

#Slight variation with regard to order and handling of edge cases. Basically removing edge case from before for loop to after the for loop

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