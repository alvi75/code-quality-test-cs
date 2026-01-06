def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	try:
		webfinger = json.loads(document)
	except ValueError as e:
		raise ValueError("Invalid JSON for Diaspora WebFinger") from e

	if "links" not in webfinger or "hcard_url" not in webfinger["links"]:
		raise ValueError("WebFinger does not contain a valid link to hcard")

	hcard_url = webfinger["links"]["hcard_url"]
	return {"href": hcard_url}