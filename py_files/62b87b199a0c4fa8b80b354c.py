def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, Sequence):
		return seq, type(seq)
	elif hasattr(seq, '__iter__'):
		return list(seq), type(list(seq))
	else:
		raise TypeError("Expected a sequence or iterable")