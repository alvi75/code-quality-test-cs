def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	try:
		webfinger = json.loads(document)
	except ValueError as e:
		raise ValueError("Invalid webfinger document") from e

	if "links" not in webfinger:
		raise ValueError("Webfinger document does not contain links")

	for link in webfinger["links"]:
		if link["rel"] == "self":
			return {
				"hcard_url": link["href"],
				"webfinger": webfinger,
			}

	raise ValueError("Webfinger document does not contain a self link")