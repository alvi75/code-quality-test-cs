def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	webfinger = json.loads(document)
	if "links" in webfinger:
		for link in webfinger["links"]:
			if link["rel"] == "hcard":
				return {"hcard_url": link["href"]}
	return {}