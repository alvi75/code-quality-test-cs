def try_retrieve_webfinger_document(handle: str) -> Optional[str]:
	"""
	Try to retrieve an RFC7033 webfinger document. Does not raise if it fails.
	"""
	try:
		response = requests.get(
			f"https://rfc7033.org/webfinger/{handle}",
			headers={"Accept": "application/rfc7033+json"},
		)
		if response.status_code == 200:
			return response.text
	except Exception as e:
		pass

	return None