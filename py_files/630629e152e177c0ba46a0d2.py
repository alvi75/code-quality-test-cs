def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "https://diasp.local/%s" % handle
	try:
		response = requests.get(url)
	except Exception as e:
		raise e

	if response.status_code == 200:
		return json.loads(response.text)