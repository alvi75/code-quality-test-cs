def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	try:
		request.json()
	except (ValueError, TypeError):
		return False

	if not isinstance(request.json(), list):
		return False

	return all('event' in event for event in request.json())