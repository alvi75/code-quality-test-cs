def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if not isinstance(seq, list):
		return False

	for item in seq:
		if not isinstance(item, FillRequest):
			return False

	return True