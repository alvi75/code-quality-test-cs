def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	url = "https://{host}/.well-known/host-meta.json".format(host=host)
	response = requests.get(url)
	if response.status_code != 200:
		raise DiasporaError("Could not retrieve host-meta document from {host}".format(host=host))
	return xrd.parse_xrd(response.text)