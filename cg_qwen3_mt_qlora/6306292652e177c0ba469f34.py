def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		response = requests.head(url, headers=HEADERS)
	except Exception as e:
		print(e)
		return None

	if response.status_code == 200:
		content_type = response.headers.get('content-type')
		if content_type is not None:
			return content_type.split(';')[0]
	else:
		return None