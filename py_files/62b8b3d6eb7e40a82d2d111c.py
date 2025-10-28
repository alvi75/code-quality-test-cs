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
		return _normalizeargs(*sequence)

	if isinstance(sequence[0], Interface):
		return _normalizeargs(*sequence)

	if isinstance(sequence[0], (tuple, list)):
		return [i for i in sequence if isinstance(i, Interface)]

	if isinstance(sequence[0], (tuple, list)):
		return [i for i in sequence if isinstance(i, Interface) or i is None]

	if isinstance(sequence[0], Interface):
		return [Sequence([i]) for i in sequence]

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple, list)):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], Interface):
		return Sequence([Sequence(i) for i in sequence])

	if isinstance(sequence[0], (tuple,