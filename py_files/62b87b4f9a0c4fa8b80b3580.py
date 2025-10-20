def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return sum([bin_integral(bins[i], bins[i+1]) for i in range(len(bins)-1)])