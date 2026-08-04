def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	if document_path is None:
		document_path = urljoin(url, WELL_KNOWN_PATH)
	try:
		response = requests.get(document_path)
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		if e.response.status_code == 404:
			return None
		else:
			raise
	except requests.exceptions.RequestException as e:
		raise
	else:
		return {
			'url': url,
			'document_path': document_path,
			'content': response.content,
			'headers': response.headers,
		}