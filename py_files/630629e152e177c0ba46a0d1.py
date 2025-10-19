def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
	"""
	Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
	"""
	try:
		response = requests.get(get_webfinger_url(handle))
		if response.status_code == 200:
			return response.text
	except Exception as e:
		logging.exception("try_retrieve_webfinger_document failed for %s: %s", handle, e)
	return None