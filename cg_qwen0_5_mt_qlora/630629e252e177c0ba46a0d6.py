def retrieve_diaspora_host_meta(host):
	"""
	Retrieve a remote Diaspora host-meta document.

:arg host: Host to retrieve from
:returns: ``XRD`` instance
	"""

	# Retrieve meta data for this host
	meta = get_diaspora_host_meta(host)

	# If we have no meta data, return None
	if not meta:
		return None

	# Create a new XRD instance
	xrd = XRD()

	# Add the meta data
	for key in meta.keys():
		xrd[key] = meta[key]

	# Return the XRD instance
	return xrd