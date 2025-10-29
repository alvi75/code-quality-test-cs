def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = 'https://webfinger.diaspora.net/1.0/webfinger?resource=acct:%s' % handle
	return parse_diaspora_webfinger(retrieve(url))