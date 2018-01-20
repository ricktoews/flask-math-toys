import unittest

from math_toys import tri
from math_toys import phi

class TestMathToys(unittest.TestCase):

	def test_tri(self):
		self.assertEqual(tri.nth_tri(5), 15)

	def test_n_tris(self):
		self.assertEqual(tri.first_n_tris(4), [1, 3, 6, 10])


	def test_phi(self):
		self.assertEqual(phi.nth(5), [11, 5])

	def test_n_phis(self):
		self.assertEqual(phi.first_n(3), [[1, 1], [3, 1], [4, 2]])

if __name__ == '__main__':
    unittest.main()

