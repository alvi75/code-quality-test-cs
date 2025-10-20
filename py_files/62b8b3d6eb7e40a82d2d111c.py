def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""

	if isinstance(sequence, tuple) and len(sequence) == 2:
		return sequence[0], sequence[1]

	elif isinstance(sequence, list):
		for i in range(len(sequence)):
			try:
				sequence[i] = _normalizeargs(sequence[i])
			except TypeError as e:
				raise TypeError("Invalid argument: %s" % str(e))

	else:
		if not isinstance(sequence, Declaration):
			# Expand interface spec to a list of interfaces
			interfaces = []
			for i in sequence.split(','):
				i = i.strip()
				if i.startswith('!'):
					interfaces.append(Not(i[1:].strip()))
				elif i.startswith('~'):
					interfaces.append(Negate(i[1:].strip()))
				else:
					interfaces.append(i)
			sequence = interfaces

		if isinstance(sequence, list):
			output = []

			for i in sequence:
				if isinstance(i, Declaration):
					output.append(i)

				elif isinstance(i, tuple):
					output.extend(_normalizeargs(i))
				else:
					output.append(i)

			return tuple(output)

		else:
			return sequence