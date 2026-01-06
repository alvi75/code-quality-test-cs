def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return sum([edges[i+1]-edges[i] for i in range(len(edges)-1)])