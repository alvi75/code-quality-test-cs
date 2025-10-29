def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if isinstance(sequence, (tuple, list)):
		return tuple(_normalizeargs(item) for item in sequence)
	elif isinstance(sequence, dict):
		return {key: _normalizeargs(value) for key, value in sequence.items()}
	elif isinstance(sequence, Interface):
		return Sequence([sequence])
	elif isinstance(sequence, Tuple):
		return Sequence([_normalizeargs(item) for item in sequence])
	else:
		if output is None:
			output = []
		output.append(sequence)
		return output