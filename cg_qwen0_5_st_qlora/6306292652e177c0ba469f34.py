def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	content_type = None

	if not url:
		return content_type

	try:
		response = requests.head(url, headers={'User-Agent': USER_AGENT})
	except Exception as e:
		logger.error("Error fetching content type for %s", url)
		return content_type

	if response.status_code == 200:
		content_type = response.headers.get('content-type')
	else:
		logger.error("Error fetching content type for %s", url)
		return content_type

	return content_type