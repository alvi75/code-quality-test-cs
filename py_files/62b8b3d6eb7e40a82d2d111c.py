def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not output:
		output = []
	for arg in sequence:
		if isinstance(arg, tuple):
			output.extend(_normalizeargs(arg))
		elif isinstance(arg, Interface):
			output.append(arg)
		else:
			raise TypeError("Invalid argument type: %s" % type(arg))
	return output