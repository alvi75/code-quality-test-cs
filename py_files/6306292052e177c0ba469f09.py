def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	body = json.loads(request.body.decode('utf-8'))
	if 'events' in body:
		return True

	if 'env' in body:
		if body['env'] == Magic_ENV_TAG:
			return True
	else:
		return False