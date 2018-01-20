#
# Math Toys. Triangular numbers
#

# Nth triangular number
def nth_tri(n):
	_tri = (n*n + n) / 2
	return _tri

# First n triangular numbers
def first_n_tris(n):
	_tris = []
	for i in xrange(0, n):
		_tris.append(nth_tri(i+1))
	return _tris


