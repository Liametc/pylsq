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
random.seed(1)

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
#pprint.pprint(results)

'''
def getRangeStr(items):
    if not items:
        return
    def func(items):
        return items[1] - items[0]
    x = [int(a) for a in sorted(items)]

    groups = []
    prev = set()
    for index, (id_, g) in enumerate(itertools.groupby(itertools.izip(x[:-1], x[1:]), func)):
        this_grp = set()
        for item in g:
                this_grp.update(item)
        if len(this_grp) <= 2 and id_ == 1:
            continue
        prev.difference_update(this_grp)
        groups.append((id_, this_grp))
        prev = this_grp

    frame_str = ''
    first = ''
    for step, frange in groups:
        frame_str += first
        first = ','
        if len(frange) == 1:
                frame_str += '{0}'.format(next(iter(frange)))
        elif step == 1:
                frame_str += '{0}-{1}'.format(min(frange), max(frange))
        else:
                frame_str += '{0}-{1}x{2}'.format(min(frange), max(frange), step)
    return frame_str
#print getRangeStr(results.keys())
'''
from pypathtools.range_object import SubRange
print 'foo'
r1 = SubRange(1,10)
r1.add_sub_range(SubRange(2, 8, 2))
for item in r1.range():
    print item

