def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	if len(edges) == 0:
		return 0

	integral = 0
	for i in range(len(edges)-1):
		integral += (edges[i+1] - edges[i]) * bins[i]

	return integral