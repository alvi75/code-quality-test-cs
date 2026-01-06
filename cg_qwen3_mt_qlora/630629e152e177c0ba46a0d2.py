def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = 'https://{}/.well-known/webfinger'.format(handle)
	response = requests.get(url, headers={'Accept': 'application/jrd+json'})
	if response.status_code != 200:
		raise ValueError('Webfinger request failed with status code {}'.format(response.status_code))
	return response.json()