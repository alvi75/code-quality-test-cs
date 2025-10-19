def _get_seq_with_type(seq, bufsize=None):
	"""
	Return a (sequence, type) pair.
Sequence is derived from *seq*
(or is *seq*, if that is of a sequence type).
	"""
	if isinstance(seq, str):
		seq = seq.encode('ascii')
	elif not hasattr(seq, 'decode'):
		raise TypeError("object of type '{}' has no decode() method".format(type(seq)))
	if isinstance(seq, bytes):
		pass
	elif sys.version_info[0] == 2:
		seq = seq.decode('ascii', errors='replace')
	else:
		seq = seq.decode('utf-8', errors='replace')
	return seq, type(seq)