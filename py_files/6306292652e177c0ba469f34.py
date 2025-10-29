def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		req = requests.head(url, headers={'User-Agent': USER_AGENT})
	except Exception as e:
		return None

	if req.status_code == 200:
		return req.headers.get('content-type')
	else:
		return None