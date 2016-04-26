string = raw_input()
temp = ''
count = 0
output = ''

for x in range(len(string)):
	if x == 0:
		temp = string[x]
		count += 1
	elif string[x] == temp:
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