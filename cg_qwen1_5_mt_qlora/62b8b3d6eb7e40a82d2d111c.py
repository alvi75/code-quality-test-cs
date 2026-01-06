def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single
interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence:
		return []

	interfaces = []
	for arg in sequence:
		if isinstance(arg, tuple) and len(arg) == 2:
			interface, args = arg
			interfaces.append((interface, args))
		elif isinstance(arg, Interface):
			interfaces.append((arg, None))
		else:
			interfaces.append((arg, None))

	if output is None:
		output = []

	for interface, args in interfaces:
		if args is None:
			args = [output]
		else:
			args = list(args)
		output.extend(args)

	return output