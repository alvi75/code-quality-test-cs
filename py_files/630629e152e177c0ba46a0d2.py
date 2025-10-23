def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""

	url = 'https://{}.{}/.well-known/webfinger'.format(handle.split('@')[1], handle.split('@')[0])
	response = requests.get(url)
	if response.status_code == 200:
		return json.loads(response.text)
	else:
		raise ValueError('Webfinger request failed with status code {}'.format(response.status_code))