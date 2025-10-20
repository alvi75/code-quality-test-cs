def retrieve_and_parse_diaspora_webfinger(handle):
	"""
	Retrieve a and parse a remote Diaspora webfinger document.

:arg handle: Remote handle to retrieve
:returns: dict
	"""

	url = "https://diasp.local/diaspora/public_key.php?handle={}".format(handle)
	try:
		response = requests.get(url, timeout=10)
	except requests.exceptions.RequestException as e:
		raise WebFingerError("Failed to retrieve diaspora public key for {}.".format(handle), e)

	if response.status_code != 200:
		raise WebFingerError("Diaspora server returned status code {}".format(response.status_code))

	return json.loads(response.text)