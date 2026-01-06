def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarations, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []
	if isinstance(sequence, (list, tuple)):
		return [ _normalizearg(arg) for arg in sequence ]
	else:
		return [ _normalizearg(sequence) ]