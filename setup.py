from setuptools import setup
import unittest

def rest_test_suite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('test', pattern='test_*.py')
	return test_suite

setup(
	name='MathToys',
	version='0.1dev',
	packages=['math_toys',],
	test_suite='setup.rest_test_suite',
)
