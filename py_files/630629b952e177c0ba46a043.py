def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	if not document_path:
		document_path = os.path.join(os.path.dirname(__file__), 'well-known', 'nodeinfo2.yml')

	with open(document_path) as f:
		document = yaml.load(f)

	document['metadata'] = {
		'url': url,
		'version': 1
	}

	return document