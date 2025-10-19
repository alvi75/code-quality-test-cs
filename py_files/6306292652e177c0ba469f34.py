def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	try:
		request = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
		response = urllib.request.urlopen(request)
	except Exception as e:
		print(e)
		return None

	return response.info().get('Content-Type')