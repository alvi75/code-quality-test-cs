def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, Sequence):
		return seq, type(seq)
	elif isinstance(seq, str):
		return StringIO(seq), str
	elif isinstance(seq, bytes):
		return BytesIO(seq), bytes
	elif isinstance(seq, Iterable):
		return _get_seq_with_type(list(seq), bufsize)
	else:
		raise TypeError("Expected sequence or string, got %r" % type(seq))