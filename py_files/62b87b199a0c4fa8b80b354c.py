def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, SequenceType):
		return seq, type(seq)
	else:
		return _get_seq_with_type(_get_sequence_from_object(seq), bufsize)