def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	try:
		data = json.loads(document)
	except ValueError as e:
		raise DiasporaInvalidDocumentError(e)

	if not data.get('webfinger'):
		raise DiasporaInvalidDocumentError("No webfinger found")

	return {
		'hcard_url': data['webfinger'].get('href'),
	}