def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	return _send_request(
		url,
		method,
		data=data,
		timeout=timeout,
		content_type="application/x-www-form-urlencoded",
		*args,
		**kwargs)