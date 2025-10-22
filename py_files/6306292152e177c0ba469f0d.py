def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if isinstance(request.body, str):
		return json.loads(request.body).get('events', None) is not None
	else:
		return False