def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if isinstance(seq, (list, tuple)):
		return True
	elif isinstance(seq, str) and seq.isdigit():
		return True
	else:
		return False