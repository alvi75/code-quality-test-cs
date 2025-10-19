def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""
	url = "https://{}/.well-known/webfinger?resource=acct:{}&resolver=".format(
		handle.split("@")[1], handle.split("@")[0]
	)
	resp = requests.get(url, verify=False)

	if resp.status_code == 200:
		return parse_diaspora_webfinger(resp.content)
	else:
		raise Exception("Error retrieving webfinger")