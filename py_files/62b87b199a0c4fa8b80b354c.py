def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, basestring):
		return seq, str
	elif hasattr(seq, 'read'):
		return seq, io.BytesIO
	else:
		try:
			seq = list(seq)
		except TypeError:
			pass
		if not isinstance(seq, SequenceType):
			raise ValueError("Expected sequence or file-like object")
		return seq, None