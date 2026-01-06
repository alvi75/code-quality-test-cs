def _get_seq_with_type(seq, bufsize=None):
	"""Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, Sequence):
		return seq, type(seq)
	elif isinstance(seq, str):
		return seq, type(seq)
	else:
		raise TypeError("Can't get sequence with type %s" % type(seq))