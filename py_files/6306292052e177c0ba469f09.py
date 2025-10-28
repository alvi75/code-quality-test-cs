def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	if isinstance(request.body, str) or isinstance(request.body, bytes):
		try:
			json.loads(request.body)
			return True
		except ValueError:
			pass

	xml = etree.fromstring(request.body)

	if xml.tag == Magic_ENV_TAG:
		return True

	return False