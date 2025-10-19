def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	data = json.loads(document)
	if "links" not in data:
		raise ValueError("No links")
	result = {}
	for link in data["links"]:
		if link["rel"] == "hcard":
			result["hcard_url"] = link["href"]
	return result