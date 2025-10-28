def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		response = requests.head(url, headers={'User-Agent': USER_AGENT})
	except Exception as e:
		return None

	if response.status_code == 200:
		content_type = response.headers.get('content-type')
		if content_type is not None:
			return content_type
	else:
		return None