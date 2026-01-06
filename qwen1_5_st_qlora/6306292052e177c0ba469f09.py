def identify_request(request: RequestType):
	"""
	Check whether the request body loaded using JSON contains events. If yes, True is returned, otherwise, check whether the tag of the XML loaded from the request body is Magic_ENV_TAG, if yes, return True. If neither of the preceding conditions is met, return False.
	"""
	if isinstance(request.body, dict) and 'events' in request.body:
		return True

	try:
		xml = ET.fromstring(request.body)
	except Exception as e:
		logger.error('Error when parsing the request body to XML:\n{}'.format(e))
		return False

	if xml.tag == Magic_ENV_TAG:
		return True

	return False