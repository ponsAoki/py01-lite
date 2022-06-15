import sys
import math

args = sys.argv

print(args[1])
r = float(args[1])

area = math.pi * r * r

print('{0}'.format(area))