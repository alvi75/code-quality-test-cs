def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	if not url:
		return None

	content_type = None
	try:
		response = requests.head(url, headers={'User-Agent': USER_AGENT})
		content_type = response.headers.get('content-type')
	except Exception as e:
		logger.error(e)
		pass

	return content_type