def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""

	if isinstance(seq, str):
		seq = seq.encode('utf-8')
	elif not isinstance(seq, bytes):
		raise TypeError("expected string or bytes-like object, got %s" %
			type(seq).__name__)

	if bufsize is None:
		bufsize = len(seq)

	# If we have a buffer, use it.
	if hasattr(seq, 'buffer'):
		return (seq.buffer(), type(seq))

	# Otherwise, create a new buffer.
	else:
		return (bufsize * [None], type(seq))