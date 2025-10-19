def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return np.sum((edges[1:] + edges[:-1]) * (bins - bins.astype(int)))