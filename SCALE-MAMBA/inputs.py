import random
import sys

u = int(sys.argv[1])
with open('input_1.txt', 'w') as f:
    for _ in range(u):
        input_arr = random.sample(range(0, u), u)
        for line in input_arr:
            f.write(str(line))
            f.write('\n')

    for _ in range(u):
        input_arr = random.sample(range(0, u), u)
        for line in input_arr:
            f.write(str(line))
            f.write('\n')
