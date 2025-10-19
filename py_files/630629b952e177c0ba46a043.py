def get_nodeinfo_well_known_document(url, document_path=None):
	'''
	Returns a formatted dictionary, including information such as url and document_path.
	'''
	document = None

	if document_path is not None:
		document = open(document_path, 'r').read()

	try:
		response = urlopen(url)
	except Exception as e:
		return {
			'error': str(e),
			'status': 500,
			'timestamp': datetime.datetime.now().isoformat()
		}

	wkb = response.read()
	wkb = wkb.decode('utf-8')

	try:
		node_info = json.loads(wkb)
	except Exception as e:
		return {
			'error': str(e),
			'status': 400,
			'timestamp': datetime.datetime.now().isoformat()
		}

	if node_info.get('status') == 200:
		node_info['url'] = url
		node_info['document_path'] = document_path
	else:
		return {
			'error': node_info.get('error', 'Unknown error'),
			'status': node_info.get('status', 500),
			'timestamp': datetime.datetime.now().isoformat()
		}

	return node_info