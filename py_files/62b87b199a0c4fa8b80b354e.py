def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if isinstance(seq, FillRequestSeq):
		return True
	elif isinstance(seq, list) or isinstance(seq, tuple):
		for item in seq:
			if not isinstance(item, FillRequest):
				return False
		return True
	else:
		return False