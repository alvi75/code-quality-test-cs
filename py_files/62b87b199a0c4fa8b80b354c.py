def _get_seq_with_type(seq, bufsize=None):
	"""Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, str):
		return seq, str
	elif hasattr(seq, 'read'):
		return seq.read(), type(seq)
	elif hasattr(seq, '__iter__') and not hasattr(seq, '__getitem__'):
		return ''.join(seq), type(seq)
	else:
		raise TypeError('Cannot convert %r to sequence' % (seq,))