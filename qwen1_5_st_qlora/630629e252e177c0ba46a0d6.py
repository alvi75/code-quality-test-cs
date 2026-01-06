def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""

	try:
		response = requests.get('https://{0}/host-meta.xrd'.format(host))
	except Exception as e:
		raise XRDException(e)

	if response.status_code != 200:
		raise XRDException(response.text)

	return XRD.from_string(response.content)