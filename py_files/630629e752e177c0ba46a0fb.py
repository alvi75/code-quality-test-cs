def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	if not isinstance(data, dict) or not isinstance(data, list):
		data = {"data": data}
	return _send_request(url, data, method, timeout, *args, **kwargs)