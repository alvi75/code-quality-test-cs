def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	if not isinstance(data, dict):
		data = json.loads(data)
	return _send_request(url, data=data, timeout=timeout, method=method, *args, **kwargs)