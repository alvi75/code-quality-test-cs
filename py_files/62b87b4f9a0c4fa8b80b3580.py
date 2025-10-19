def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return sum([bin_width * bin_height for (bin_width, bin_height) in zip(edges[1:], bins[:-1])])