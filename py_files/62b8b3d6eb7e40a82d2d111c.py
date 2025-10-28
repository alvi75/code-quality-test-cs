def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []

	if isinstance(sequence[0], tuple):
		# Expand all tuples in sequence
		result = []
		for item in sequence:
			result.extend(_expand(item))
		return result

	elif isinstance(sequence[0], Interface):
		# Expand all interfaces in sequence
		result = []
		for item in sequence:
			result.append(item)
		return result

	else:
		# Expand all items in sequence
		result = []
		for item in sequence:
			result.extend(_expand(item))
		return result