#
# Math Toys. Phi
#

import math

ROOT5 = math.sqrt(5)

def fib(starter, n):
	if n <= 2:
		_f = starter[n-1]
	else:
		_f = fib(starter, n-2) + fib(starter, n-1)
	return _f

# Nth power of phi
def nth(n):
	_a = fib([1, 3], n)
	_b = fib([1, 1], n)
	_str = '(%d + %dsqrt5) / 2' % (_a, _b)
	_obj = {}
	_obj['phi_num'] = { 'sqrt_5_coef': _b, 'whole': _a }
	_obj['power'] = n
	_obj['real_value'] = (_a + _b*ROOT5) / 2
	return _obj

# First n powers of phi
def first_n(n):
	_phis = []
	for i in xrange(0, n):
		_phis.append(nth(i+1))
	return _phis


