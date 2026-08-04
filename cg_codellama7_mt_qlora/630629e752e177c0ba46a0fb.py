def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	if method == "post":
		return send_post(url, data, timeout, *args, **kwargs)
	elif method == "get":
		return send_get(url, data, timeout, *args, **kwargs)
	else:
		raise ValueError("Invalid method: %s" % method)