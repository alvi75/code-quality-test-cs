def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	document = json.loads(document)
	webfinger = document['webfinger']
	hcard_url = webfinger.get('hcard_url')
	if not hcard_url:
		raise ValueError("WebFinger does not contain a hcard_url")
	return {
		'hcard_url': hcard_url,
		'href': webfinger['links'][0]['href'],
	}