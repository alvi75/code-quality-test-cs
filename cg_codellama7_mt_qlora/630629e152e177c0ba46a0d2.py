def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "https://%s/.well-known/webfinger?resource=acct:%s" % (handle, handle)
	response = requests.get(url)
	if response.status_code != 200:
		raise DiasporaError("Could not retrieve webfinger document for %s" % handle)
	return json.loads(response.content)