def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	url = 'https://{host}/.well-known/host-meta'.format(host=host)
	return XRD(url)