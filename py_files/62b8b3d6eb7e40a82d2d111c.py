def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarations, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []
	if isinstance(sequence, (tuple, list)):
		return [normalizearg(x) for x in sequence]
	else:
		return [normalizearg(sequence)]