def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	if not host:
		raise ValueError("Host is required")
	try:
		return requests.get(
			"http://{}{}".format(host, "/meta").encode('utf-8')
		).json()
	except Exception as e:
		raise ValueError("Unable to retrieve meta data for {} - {}".format(host, e))