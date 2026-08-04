def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, (list, tuple)):
		seq_type = type(seq)
		seq = list(seq)
	elif isinstance(seq, (str, bytes)):
		seq_type = type(seq)
		seq = list(seq)
	else:
		seq_type = type(seq)
		seq = [seq]
	return seq, seq_type