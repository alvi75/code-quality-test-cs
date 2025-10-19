def is_fill_request_seq(seq):
	"""
	Check whether seq can be converted to FillRequestSeq and bool is returned.
	"""
	try:
		if isinstance(seq, (list, tuple)):
			for i in seq:
				FillRequest(i)
		else:
			raise TypeError("seq must be list or tuple")
	except:
		return False

	return True