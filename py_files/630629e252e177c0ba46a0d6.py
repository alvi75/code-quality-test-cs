def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	if not host:
		return None

	resp = requests.get(
		"http://{}{}".format(DIASPORA_HOST, host),
		headers={"Accept": "application/xml"},
		stream=True,
	)
	resp.raise_for_status()
	return xrd_from_xml(resp.content)