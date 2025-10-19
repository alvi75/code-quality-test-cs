def _replace_url_args(url, url_args):
	"""
	Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
	if not url_args:
		return url

	url_components = list(urlparse(url))
	query = dict(parse_qsl(url_components[4]))
	for key, value in url_args.items():
		if value is None:
			del query[key]
		else:
			query[key] = value
	url_components[4] = urlencode(query)
	return urlunparse(url_components)