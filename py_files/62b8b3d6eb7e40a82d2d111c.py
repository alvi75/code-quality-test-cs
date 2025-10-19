def _normalizeargs(sequence, output=None):
	"""
	Normalize declaration arguments

Normalization arguments might contain Declarions, tuples, or single interfaces.

Anything but individial interfaces or implements specs will be expanded.
	"""
	if not sequence: return ()
	if isinstance(sequence, Declaration): return (sequence,)
	if isinstance(sequence, tuple): return sequence
	if isinterface(sequence): return (sequence,)
	if istype(sequence): return _normalizeargs(declaresequence(sequence))
	if isimplements(sequence): return (sequence.interface,)
	return ()