def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if request.method == 'POST':
		try:
			data = json.loads(request.body.decode('utf-8'))
			if isinstance(data, list):
				return True
		except ValueError:
			pass
	return False