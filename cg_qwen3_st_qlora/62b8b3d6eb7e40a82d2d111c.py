def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []

	if isinstance(sequence, (tuple, list)):
		return [ _normalizeargs(s) for s in sequence ]

	if isinstance(sequence, Declaration):
		return [ sequence ]

	if isinstance(sequence, ImplementsSpec):
		return [ sequence ]

	if isinstance(sequence, Interface):
		return [ sequence ]

	raise TypeError("Invalid argument type: %s" % type(sequence))