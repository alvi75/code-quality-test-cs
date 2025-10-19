def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if isinstance(seq, FillRequestSeq):
		return True, seq
	elif isinstance(seq, list) and len(seq) == 1:
		return True, FillRequestSeq([seq[0]])
	else:
		return False, None