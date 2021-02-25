import unittest
import pytest
import fibonacci

class TestCaseFibonacci(unittest.TestCase):

	#test base cases
	def testFibBaseCase(self):
		self.assertEqual(fibonacci.fibonacci(1), 0)
		self.assertEqual(fibonacci.fibonacci(2), 1)

	#test more general cases
	def testFib(self):
		self.assertEqual(fibonacci.fibonacci(3), 1)
		self.assertEqual(fibonacci.fibonacci(4), 2)
		self.assertEqual(fibonacci.fibonacci(8), 13)
		self.assertEqual(fibonacci.fibonacci(10), 34)


	def testFacBaseCase(self):
		self.assertEqual(fibonacci.factorial(0),1)
		self.assertEqual(fibonacci.factorial(1),1)


	def testFac(self):
		self.assertEqual(fibonacci.factorial(2),2)
		self.assertEqual(fibonacci.factorial(3),6)
		self.assertEqual(fibonacci.factorial(4),24)
		self.assertEqual(fibonacci.factorial(5),120)


if __name__ == '__main__':
	unittest.main()



def test_answer():
	assert fibonacci.fibonacci(8) == 13
