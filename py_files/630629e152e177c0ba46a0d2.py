def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "https://diaspora.{}".format(settings.DOMAIN)
	response = requests.get(url, params={"handle": handle})
	if response.status_code == 200:
		return json.loads(response.text)