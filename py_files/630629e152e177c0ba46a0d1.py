def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
	"""
	Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
	"""
	try:
		return get_webfinger_document(handle)
	except Exception as e:
		log.error("Failed to retrieve webfinger document for %s", handle, exc_info=True)