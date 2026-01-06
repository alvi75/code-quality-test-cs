def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	if not isinstance(request.body, bytes):
		return False

	try:
		request_body = json.loads(request.body.decode('utf-8'))
	except ValueError:
		return False

	for event in request_body:
		if 'type' in event and 'name' in event['type'] and 'args' in event['type']['name']:
			return True

	return False