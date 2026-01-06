def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	if len(edges) == 1:
		return np.sum((edges[0] - bins[0]) * (bins[-1] - bins[0]))
	else:
		integral = 0
		for i in range(len(edges)-2):
			integral += (edges[i+1]-edges[i])*(np.sum(bins[i+1:])-np.sum(bins[i:i+1]))
		return integral