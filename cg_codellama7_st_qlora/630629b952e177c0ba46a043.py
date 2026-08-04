def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	if document_path is None:
		document_path = url + "/.well-known/nodeinfo"
		
	try:
		response = requests.get(document_path)
		response.raise_for_status()
	except requests.exceptions.HTTPError as e:
		if e.response.status_code == 404:
			return None
		else:
			raise
	except requests.exceptions.ConnectionError as e:
		raise
	
	return {
		"url": url,
		"document_path": document_path,
		"document": response.text
	}