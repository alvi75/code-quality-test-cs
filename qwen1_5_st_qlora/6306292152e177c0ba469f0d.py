def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if isinstance(request.body, str):
		try:
			json.loads(request.body)
			return True
		except ValueError:
			pass

	return False