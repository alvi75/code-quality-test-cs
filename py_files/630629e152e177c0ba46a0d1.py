def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
	"""
	Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
	"""
	try:
		response = requests.get(f"https://webfinger.{handle}.net/.well-known/webfinger")
		if response.status_code == 200:
			return response.text
	except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
		pass
	return None