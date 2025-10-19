def identify_request(request: RequestType) -> bool:
		"""
		Check whether the request body loaded using JSON contains events. If yes, True is returned. Otherwise, False is returned.
		"""
		if not isinstance(request.body, str):
			return False

		try:
			request_body = json.loads(request.body)
		except ValueError as e:
			return False

		if 'events' in request_body:
			return True
		else:
			return False

	return identify_request