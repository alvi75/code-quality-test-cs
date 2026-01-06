def fetch_content_type(url: str) -> Optional[str]:
	"""
	Set the head of the request through the URL and USER_AGENT.
	"""
	if not url:
		return None

	# set user agent
	user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.409.27 Safari/537.36"
	headers = {"User-Agent": user_agent}

	# set content type
	content_type = "text/html"

	# send a GET request to the URL
	r = requests.get(url, headers=headers)

	# check if the response is OK
	if r.status_code != 200:
		return None

	# get the content type from the response
	content_type = r.headers["content-type"]

	# return the content type
	return content_type