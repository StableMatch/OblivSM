import random
import sys
no_of_players = int(sys.argv[1])

input_data = []
base = list(range(0,no_of_players))


for i in range(no_of_players):
	data = base.copy()
	random.shuffle(data)
	input_data += [data]

with open('Input-P0-0', 'w') as file:
	for i in input_data:
		#print(" ".join(input_data[i]))
		file.write(" ".join(map(str, i)))
		file.write('\n')

input_data = []
base = list(range(0,no_of_players))

for i in range(no_of_players):
	data = base.copy()
	random.shuffle(data)
	input_data += [data]

with open('Input-P1-0', 'w') as file:
	for i in input_data:
		#print(" ".join(input_data[i]))
		file.write(" ".join(map(str, i)))
		file.write('\n')

