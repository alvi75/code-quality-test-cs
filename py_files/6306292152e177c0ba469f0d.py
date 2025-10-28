def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	try:
		json.loads(request.body)
	except ValueError as e:
		return False

	if 'events' in json.loads(request.body):
		return True
	else:
		return False