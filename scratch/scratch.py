import sys

sys.path.append('/home/liam/git/pypathtools/python')

import pypathtools

pad = pypathtools.PadObject(5)
print pad.getRegexPattern()

