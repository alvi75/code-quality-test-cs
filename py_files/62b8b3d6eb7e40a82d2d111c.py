def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []
	output = [] if output is None else output[:]
	for arg in sequence:
		if isinstance(arg, Interface) and len(arg.interfaces) == 1:
			arg = arg.interfaces[0]
		elif isinstance(arg, (Interface, Class)):
			continue
		else:
			arg = [arg]
		for i in arg:
			i = _normalize(i)
			if i is not None:
				output.append(i)
	return output