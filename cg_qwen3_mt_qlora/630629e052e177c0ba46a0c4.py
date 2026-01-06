def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	try:
		webfinger = json.loads(document)
	except ValueError as e:
		raise WebFingerError("Invalid JSON document: {}".format(e))

	if "links" not in webfinger:
		raise WebFingerError("No links found")

	for link in webfinger["links"]:
		if link["rel"] == "urn:converse:hcard":
			return {"hcard": link["href"]}
	else:
		raise WebFingerError("No hcard URL found")