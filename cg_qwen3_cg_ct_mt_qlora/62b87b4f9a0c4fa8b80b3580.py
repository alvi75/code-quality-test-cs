def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return np.trapz(bins, x=edges)