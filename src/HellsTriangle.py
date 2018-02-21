class HellsTriangle(object):

	def __init__(self, triangle):
		self.triangle = triangle
		self.nRows = len(self.triangle)

	def setTriangle(self,triangle):
		self.triangle = triangle
		self.nRows = len(self.triangle)

	def getMaxTotal(self):
		actual = self.triangle[0].copy()

		for i in range(1, self.nRows):
			previous = actual
			actual = self.triangle[i].copy()

			nCols = len(actual)
			actual[0] += previous[0]
			for j in range(1, nCols):
				actual[j] += max(previous[j-1:j+1])

		return max(actual)