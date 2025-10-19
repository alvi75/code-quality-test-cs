def send_document(url, data, timeout=10, method="post", *args, **kwargs):
	"""
	Send a response containing data through the POST method.
	"""
	return requests.post(url, data=data, headers={"Content-Type": "application/json"}, verify=False, auth=("api", API_KEY), timeout=timeout)