def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if output is None:
		output = []
	for item in sequence:
		if isinstance(item, Declaration):
			output.append(item)
		elif isinstance(item, tuple):
			_normalizeargs(item, output)
		else:
			output.append(item)
	return output