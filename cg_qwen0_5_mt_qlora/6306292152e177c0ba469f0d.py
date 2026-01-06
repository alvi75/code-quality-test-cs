def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if not isinstance(request, RequestType):
		return False

	try:
		events = json.loads(request.body)
	except ValueError:
		return False

	for event in events:
		if not isinstance(event, Event):
			return False

	return True