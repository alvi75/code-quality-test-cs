def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	try:
		return json.loads(request.body.decode('utf-8'))['events']
	except (TypeError, ValueError):
		return False