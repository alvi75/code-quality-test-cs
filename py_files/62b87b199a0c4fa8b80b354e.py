def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if isinstance(seq, (list, tuple)):
		return all(isinstance(i, int) for i in seq)
	elif isinstance(seq, int):
		return True
	else:
		return False