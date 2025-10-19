def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""
	host_meta_url = 'https://{}/host-meta'.format(host)
	try:
		response = requests.get(
			host_meta_url,
			headers={'Accept': 'application/xrds+xml, application/rdf+xml,application/xml;q=0.9,*/*;q=0.8'})
		response.raise_for_status()
	except RequestException as e:
		raise ConnectionError(e)

	return XRD.from_string(response.content)