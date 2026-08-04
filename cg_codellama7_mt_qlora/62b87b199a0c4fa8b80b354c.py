def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, (list, tuple)):
		seq = tuple(seq)
	elif isinstance(seq, (set, frozenset)):
		seq = list(seq)
	elif isinstance(seq, dict):
		seq = list(seq.items())
	elif isinstance(seq, (str, bytes)):
		seq = list(seq)
	elif isinstance(seq, (bytearray, memoryview)):
		seq = list(seq)
	elif isinstance(seq, (array.array, numpy.ndarray)):
		seq = list(seq)
	elif isinstance(seq, numpy.matrix):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.generic):
		seq = list(seq)
	elif isinstance(seq, numpy.ndarray):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.matrix):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.generic):
		seq = list(seq)
	elif isinstance(seq, numpy.ndarray):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.matrix):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.generic):
		seq = list(seq)
	elif isinstance(seq, numpy.ndarray):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.matrix):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.generic):
		seq = list(seq)
	elif isinstance(seq, numpy.ndarray):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.matrix):
		seq = list(seq.flat)
	elif isinstance(seq, numpy.generic):
		seq =