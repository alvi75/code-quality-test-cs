def paging(response, max_results):
	"""
	Return every response with the length of max_results
    Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.
	"""
	if len(response) > 0:
		yield response

	while True:
		try:
			response = yield response[-1].next()
		except StopIteration:
			break
		else:
			if len(response) == 0:
				return
			elif len(response) <= max_results:
				yield response
			else:
				yield response[:max_results]