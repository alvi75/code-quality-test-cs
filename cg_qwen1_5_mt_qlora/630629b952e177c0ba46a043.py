def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	if not document_path:
		document_path = 'nodeinfo.json'
	return {
		'url': url,
		'document_path': document_path
	}