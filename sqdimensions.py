matrix = [
	["0000011100"],
	["0011111100"],
	["0011111000"],
	["1111111100"],
	["0110000000"]
]

#find the largest square dimension of 1's
max_dim = 0 #this will change
current_dim = 0
for line in matrix:
	for element in line:
		while(element == 1):
			current_dim+=1
		check_square(current_dim)

def check_square(num):
	#given a number, verify that 