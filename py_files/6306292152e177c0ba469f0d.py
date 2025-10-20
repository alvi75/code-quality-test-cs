def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if isinstance(request, dict):
		return 'events' in request

	if isinstance(request, list):
		for item in request:
			if isinstance(item, dict):
				return 'events' in item

	return False