def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	if len(edges) != len(bins)+1:
		raise ValueError("edges must be one element longer than bins")
	return np.sum((bins[1:] - bins[:-1]) * (edges[1:] + edges[:-1])/2.)