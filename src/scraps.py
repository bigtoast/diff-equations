__author__ = 'andrew'

import numpy

p = numpy.zeros([2,3])

p[0,1] = 7.
p[1,2] = 8.

print p

p = 1. + 2. * p

print p
