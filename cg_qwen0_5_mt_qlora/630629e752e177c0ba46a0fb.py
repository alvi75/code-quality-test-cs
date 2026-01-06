def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	if not url.startswith("http"):
		url = "http://" + url

	if method == "get":
		return _send_document_get(url, data, timeout, *args, **kwargs)
	elif method == "post":
		return _send_document_post(url, data, timeout, *args, **kwargs)