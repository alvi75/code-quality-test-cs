def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	body = json.loads(request.body.decode('utf-8'))
	return any([event in body for event in EVENT_TYPES])