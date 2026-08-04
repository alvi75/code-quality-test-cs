def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	area = 0
	for i in range(len(bins)):
		area += bins[i] * (edges[i+1] - edges[i])
	return area