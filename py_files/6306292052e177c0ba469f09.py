def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	if isinstance(request.body, str) and request.body:
		try:
			data = json.loads(request.body)
		except ValueError as e:
			return False

		if 'events' in data:
			return True

		if 'tag' in data and data['tag'] == MAGIC_ENV_TAG:
			return True

		return False