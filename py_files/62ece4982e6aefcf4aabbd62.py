def _replace_url_args(url, url_args):
    """
    Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
	url = urlparse.urlparse(url)
	if not isinstance(url_args, dict):
		return url

	for k, v in list(url_args.items()):
		if k != "":
			url = url._replace(
				querystring=url._replace(querystring=url._replace(**{k:v})))

	return url.geturl()