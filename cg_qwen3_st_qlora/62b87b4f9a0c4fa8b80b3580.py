def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return sum([b * (edges[i + 1] - edges[i]) for i, b in enumerate(bins)])