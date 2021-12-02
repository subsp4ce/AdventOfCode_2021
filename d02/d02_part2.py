def	position(data_list):
	horz = 0
	depth = 0
	aim = 0
	for x in data_list:
		dir, amt = x.split()
		amt = int(amt)
		if dir == "forward":
			horz = horz + amt
			depth = depth + (aim * amt)
		if dir == "down":
			aim = aim + amt
		if dir == "up":
			aim = aim - amt
	return(horz * depth)

f = open("input.txt", "r")
data = f.read()
data_list = data.splitlines()
f.close()

print(position(data_list))