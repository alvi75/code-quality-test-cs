def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	request = requests.get(url, headers=HEADERS)
	return request.headers.get('Content-Type')