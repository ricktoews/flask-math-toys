#
# Math Toys. Phi
#

import math

ROOT5 = math.sqrt(5)

def fib(starter, n):
	if n <= 2:
		return starter[n-1]
	return fib(starter, n-2) + fib(starter, n-1)

# Nth power of phi
def nth(n):
	_a = fib([1, 3], n)
	_b = fib([1, 1], n)
	return [_a, _b]

# First n powers of phi
def first_n(n):
	_phis = []
	for i in xrange(0, n):
		_phis.append(nth(i+1))
	return _phis


