def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if isinstance(request, dict):
		return 'events' in request

	if isinstance(request, list):
		for item in request:
			if not isinstance(item, dict):
				continue

			if 'events' in item:
				return True

	return False