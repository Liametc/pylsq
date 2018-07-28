import sys
import os
import re

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'python') 
print path
sys.path.append(path)

import pypathtools
'''
pad = pypathtools.PadObject.parse_padding('#####')
regex = pad.get_regex_pattern()
print regex
match = re.search(regex, '/home/liam/foo.-1001.exr')
if match:
	print match.group(1)
'''

import itertools
import random

data = []
for i,j,k in itertools.combinations_with_replacement(xrange(1001,1010),3):
	if random.choice([True, False]):
		continue
	data.append('{0}.{1}.{2}'.format(i,j,k))


results = {}


for item in data:
	components = item.split('.')
	
	current_data = results
	for current in components:
		if not current_data.get(current):
			current_data[current] = {}
		current_data = current_data[current]
		
import pprint
pprint.pprint(results)


