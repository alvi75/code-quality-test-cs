def paging(response, max_results):
	"""
	Return every response with the length of max_results
    Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.
	"""
	if not isinstance(response, list):
		raise TypeError("response must be a list")
	if len(response) == 0:
		yield []
		return

	while True:
		yield response[0:max_results]
		response = response[max_results:]
		if len(response) == 0:
			break