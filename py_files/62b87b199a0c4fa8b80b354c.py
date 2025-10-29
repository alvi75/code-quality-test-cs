def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, str):
		return seq, str
	elif isinstance(seq, bytes):
		return seq, bytes
	else:
		try:
			seq = iter(seq)
		except TypeError:
			pass
		if not hasattr(seq, '__getitem__'):
			raise ValueError("not a sequence")
		if bufsize is None:
			bufsize = 1024
		if bufsize < 1:
			raise ValueError("invalid buffer size")
		seq = list(seq)
		if len(seq) > bufsize:
			seq = seq[:bufsize]
		return seq, type(seq[0])