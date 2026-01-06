def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		response = requests.head(
			url,
			headers={'User-Agent': USER_AGENT},
			timeout=TIMEOUT)
	except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
		return None

	if response.headers.get('content-type'):
		return response.headers['content-type']
	else:
		return None