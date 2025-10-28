def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	url = 'http://%s/.well-known/host-meta' % host
	try:
		response = requests.get(url)
	except requests.exceptions.RequestException as e:
		raise Exception('Error retrieving diaspora host-meta at %s: %s' % (url, str(e)))
	if response.status_code != 200:
		raise Exception('Error retrieving diaspora host-meta at %s: %s' % (url, response.text))
	return XRD(response.content)