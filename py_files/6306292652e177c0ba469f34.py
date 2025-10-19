def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	if not url:
		return None

	content_type = get_content_type(url)
	if content_type is None:
		content_type = DEFAULT_CONTENT_TYPE
	else:
		content_type = 'text/html; charset=utf-8'

	headers = {
		'User-Agent': f'{get_user_agent()}; {content_type}',
	}

	request = requests.Request('GET', url, headers=headers).prepare()

	return request.headers.get('Content-Type')