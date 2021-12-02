def	position(data_list):
	hor = 0
	depth = 0
	for x in data_list:
		dir, amt = x.split()
		amt = int(amt)
		if dir == "forward":
			hor = hor + amt
		if dir == "down":
			depth = depth + amt
		if dir == "up":
			depth = depth - amt
	return(hor * depth)

f = open("input.txt", "r")
data = f.read()
data_list = data.splitlines()
f.close()

print(position(data_list))