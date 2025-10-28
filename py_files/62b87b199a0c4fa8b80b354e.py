def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	if not isinstance(seq, list) or len(seq) != 2:
		return False

	fill_req = seq[0]
	fill_resp = seq[1]

	if not isinstance(fill_req, FillRequest) or not isinstance(fill_resp, FillResponse):
		return False

	return True