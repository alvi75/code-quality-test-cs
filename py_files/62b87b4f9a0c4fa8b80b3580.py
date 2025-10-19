def integral(bins, edges):
		"""Calculate the area of the overall graph."""
		return sum([np.prod((edges[i+1] - edges[i])**2) for i in range(len(edges)-1)])

	# Calculate the integral over all bins
	integral = np.zeros_like(bins)
	for i in range(len(bins)):
		integral[:,i] = integral_binned(bins[:,i], edges)

	return integral