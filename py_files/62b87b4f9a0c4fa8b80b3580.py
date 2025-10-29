def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return np.trapz(np.diff(edges), edges)