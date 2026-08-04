def identify_request(request: RequestType) -> bool:
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
	"""
	try:
		if request.json:
			if 'events' in request.json:
				return True
			else:
				return False
	except ValueError:
		return False