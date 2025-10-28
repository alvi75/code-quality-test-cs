def parse_diaspora_webfinger(document: str) -> Dict:
	"""
	The webfinger is obtained by reading the document in JSON format, the value of hcard_url in the webfinger is the value of href in links in the document.
	"""
	webfinger = json.loads(document)
	hcard_url = webfinger['subject']
	if 'links' not in webfinger or len(webfinger['links']) == 0:
		return None

	for link in webfinger['links']:
		if link['rel'] == 'http://diaspora.com/hcard':
			hcard_url = link['href']

	if hcard_url is None:
		return None

	hcard_document = get_hcard(hcard_url)

	if hcard_document is None:
		return None

	hcard = json.loads(hcard_document.decode('utf-8'))
	return {
		'name': hcard.get('name'),
		'email': hcard.get('email'),
		'url': hcard.get('url')
	}