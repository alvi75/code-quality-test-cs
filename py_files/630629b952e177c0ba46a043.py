def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	wkdn = get_well_known_document(url)
	if wkdn is None:
		return None

	document_path = document_path or os.path.dirname(wkdn)

	return {
		'url': url,
		'document_path': document_path,
	}