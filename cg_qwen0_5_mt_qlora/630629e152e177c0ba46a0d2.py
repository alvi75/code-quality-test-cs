def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""

	# Retrieve the webfinger document from the remote server.
	webfinger = get_remote_diaspora_webfinger(handle)

	# Parse the webfinger document.
	webfinger_parsed = parse_webfinger_document(webfinger)

	return webfinger_parsed