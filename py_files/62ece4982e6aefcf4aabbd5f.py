def paging(response, max_results):
    """
    Return every response with the length of max_results
    Args:
    response (list): WAPI response.
    max_results (int): Maximum number of objects to be returned in one page.
    Returns:
        Generator object with WAPI response split page by page.
	"""
    while True:
        if len(response) < max_results:
            yield response
            break

        for i in range(0, min(max_results, len(response)), max_results):
            yield response[i:i + max_results]

        # Get next page
        response = response[max_results:]