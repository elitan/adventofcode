def next_digit(sd, digit, index):
	if index < len(sd) and sd[index] == digit:
		return 1 + next_digit(sd, digit, index+1)
	return 0

sd = "1113222113"
#sd = "1"

for i in range(50):
	index = 0
	new_sd = ""
	while index < len(sd):
		nr = next_digit(sd, sd[index], index)
		new_sd += str(nr) + sd[index]
		index += nr
	sd = new_sd

print(len(sd))