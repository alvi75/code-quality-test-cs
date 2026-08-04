def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	if method == "post":
		return requests.post(url, data=data, timeout=timeout, *args, **kwargs)
	elif method == "get":
		return requests.get(url, data=data, timeout=timeout, *args, **kwargs)
	else:
		raise ValueError("Invalid method: %s" % method)