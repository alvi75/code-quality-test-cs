def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	url = "https://{0}/host-meta.xml".format(host)
	return retrieve_xrd(url)