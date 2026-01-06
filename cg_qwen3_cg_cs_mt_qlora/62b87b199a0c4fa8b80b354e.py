def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if isinstance(seq, (list, tuple)):
		return all(isinstance(i, FillRequest) for i in seq)
	else:
		return False