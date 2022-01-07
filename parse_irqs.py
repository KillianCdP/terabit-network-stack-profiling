#!/bin/python3

# Parse the output of the command `show_irq_affinity.sh` 

import math
import sys

def bitmap_to_cpu(bitmap):
	sum = 0
	for i in range(0, len(bitmap)):
		val = int(bitmap[len(bitmap)-i-1])
		if val > 0:
			sum += math.log2(val)+i*4
	return int(sum)

file = sys.argv[1]

data = {}

with open(file, "r") as f:
	lines = [line.strip('\n') for line in f.readlines()]

for line in lines:
	s = line.split(": ")
	data[int(s[0])] = s[1]

offset = min(list(map(int, data.keys())))
result = {}
for key, value in data.items():
    result[bitmap_to_cpu(value)] = int(key)-offset

print([result[key] for key in sorted(result.keys())])
