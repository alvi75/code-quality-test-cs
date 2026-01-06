def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if not isinstance(seq, FillRequestSeq):
		return False
	else:
		return True