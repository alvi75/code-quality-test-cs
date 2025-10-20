def get_nodeinfo_well_known_document(url, document_path=None):
	"""
	Returns a formatted dictionary, including information such as url and document_path.
	"""
	if not document_path:
		document_path = os.path.join(os.path.dirname(__file__), 'nodeinfo.json')
	with open(document_path) as f:
		nodeinfo = json.load(f)
	nodeinfo['links'] = [{
		'rel': 'self',
		'href': url,
	}]
	return nodeinfo