def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = 'https://webfinger.diaspora.com/' + handle
	response = requests.get(url)
	if response.status_code != 200:
		raise WebFingerError('Webfinger request failed with status code %d' % response.status_code)

	return json.loads(response.text)