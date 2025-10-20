def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""

	try:
		response = requests.get('https://{0}/host-meta'.format(host))
	except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
		raise exceptions.DiasporaHostMetaException(e)

	if response.status_code == 200:
		return XRD(response.text)
	else:
		raise exceptions.DiasporaHostMetaException(
			u'Failed to retrieve host-meta for {0}: {1}'.format(host,
				response.status_code))