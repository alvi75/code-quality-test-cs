def _normalizeargs(sequence, output=None):
		"""
		Normalize declaration arguments

Normalization arguments might contain Declarations, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if output is None:
		output = []
	for item in sequence:
		if isinstance(item, Declaration):
			output.append(_normalizeargs(item.declaration))
		elif isinstance(item, tuple) and len(item) == 1:
			output.extend(_normalizeargs(item[0]))
		else:
			output.append(item)
	return output