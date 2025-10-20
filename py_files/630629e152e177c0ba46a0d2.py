def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""

	url = "https://diaspora.mastodon.social/webfinger?resource={0}".format(
			handle)
	r = requests.get(url, headers={'Accept': 'application/json'})
	if r.status_code != 200:
		return None

	try:
		data = json.loads(r.text)
	except ValueError as e:
		logger.error("Error parsing diaspora webfinger response")
		raise e

	if not data or 'subject' not in data:
		return None

	subject = data['subject']
	if subject.startswith('acct:') is False:
		return None

	diaspora_handle = subject[5:]
	if diaspora_handle == handle:
		return data

	return None