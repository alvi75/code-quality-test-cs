def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	webfinger = get_remote_webfinger(handle)
	if not webfinger:
		return None

	webfinger_json = json.loads(webfinger)

	return webfinger_json