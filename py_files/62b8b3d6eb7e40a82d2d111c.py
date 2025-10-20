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
			output.append(_normalizeargs(arg))
		elif isinstance(arg, Declaration):
			output.append(arg)
		else:
			output.extend(_normalizeargs(arg))
	return output