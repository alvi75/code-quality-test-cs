def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	# Retrieve the webfinger document from the remote server
	webfinger = get_remote_diaspora_webfinger(handle)
	if not webfinger:
		return None

	# Parse the webfinger document
	try:
		return parse_webfinger(webfinger)
	except Exception as e:
		log.error("Error parsing webfinger document for %s: %s", handle, e)
		return None