def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "https://%s/.well-known/host-meta.json" % handle
	response = requests.get(url)
	if response.status_code != 200:
		raise DiasporaWebfingerError("Could not retrieve webfinger document from %s" % url)
	return json.loads(response.content)