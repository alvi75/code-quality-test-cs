def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return output

	if isinstance(sequence[0], Interface):
		output = [sequence[0]]
	elif isinstance(sequence[0], tuple):
		output = [sequence[0]]
	else:
		output = [Sequence(sequence)]

	for i in range(1, len(sequence)):
		if isinstance(sequence[i], Interface) and \
				not isinstance(sequence[i], tuple):
			output.append(sequence[i])
		elif isinstance(sequence[i], tuple):
			output.extend(sequence[i])

	return output