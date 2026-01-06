def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarations, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if output is None:
		output = []
	for arg in sequence:
		if isinstance(arg, tuple) or isinstance(arg, list):
			output.append(_normalizearglist(arg))
		elif isinstance(arg, Interface):
			output.append(arg)
		else:
			output.append(Declaration(arg))
	return output