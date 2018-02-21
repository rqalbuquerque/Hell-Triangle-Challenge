import unittest
from HellsTriangle import HellsTriangle

class HellsTriangleTestCase(unittest.TestCase):
	def setUp(self):
		self.hellsTriangle = HellsTriangle([[6],[3,5],[9,7,1],[4,6,8,4]])
	def testDefaultTriangle(self):
		assert self.hellsTriangle.getMaxTotal() == (26), 'incorrect max total'
	def testTriagleV1(self):
		self.hellsTriangle.setTriangle([[6]])
		assert self.hellsTriangle.getMaxTotal() == (6), 'incorrect max total'
	def testTriagleV2(self):
		self.hellsTriangle.setTriangle([[-1],[1,0],[0,0,0],[0,0,0,0],[1,0,0,0,0]])
		assert self.hellsTriangle.getMaxTotal() == (1), 'incorrect max total'
	def testTriagleV3(self):
		self.hellsTriangle.setTriangle([[7],[9,8],[5,3,4],[6,1,3,6],[7,8,2,1,10]])
		assert self.hellsTriangle.getMaxTotal() == (35), 'incorrect max total'

class HellsTriangleTestSuite(unittest.TestSuite):
   def __init__(self):
       unittest.TestSuite.__init__(self,map(HellsTriangleTestCase,
                                             ("testDefaultTriangle",
                                              "testTriagleV1",
                                              "testTriagleV2",
                                              "testTriagleV3")))

if __name__ == "__main__":
	unittest.main()

	# test_sample_1 = [[6]]
	# test_sample_2 = [[6],[3,5]]
	# test_sample_3 = [[6],[3,5],[9,7,1]]
	# test_sample_4 = [[6],[3,5],[9,7,1],[4,6,8,4]]
	# test_sample_5 = [[7],[9,8],[5,3,4],[6,1,3,6],[7,8,2,1,10]]
	# test_sample_6 = [[-1],[1,0],[0,0,0],[0,0,0,0],[1,0,0,0,0]]
	# hellsTriangle = HellsTriangle(test_sample_6)
	# hellsTriangle.setTriangle([[6]])
	# print("Max total: " + str(hellsTriangle.getMaxTotal()))
