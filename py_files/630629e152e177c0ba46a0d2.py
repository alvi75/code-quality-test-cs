def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""

	response = requests.get('https://diaspora.{0}.com/webfinger'.format(handle))
	if response.status_code != 200:
		raise DiasporaError("Failed to retrieve Diaspora WebFinger for {0}".format(handle))

	return xmltodict.parse(response.text)