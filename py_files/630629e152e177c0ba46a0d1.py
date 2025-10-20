def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
	"""
	Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
	"""
	try:
		return get_webfinger_document(handle)
	except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
		pass
	return None