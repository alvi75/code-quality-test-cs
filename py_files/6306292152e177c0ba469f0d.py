def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if not isinstance(request, RequestType):
		return False

	try:
		request_json = json.loads(request.body)
	except ValueError as e:
		return False

	if 'events' in request_json:
		return True

	return False