def _replace_url_args(url, url_args):
	"""
	Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
	if not isinstance(url_args, dict):
		raise TypeError("url_args must be a dictionary")
	for key, val in six.iteritems(url_args):
		url = url.replace(key, val)
	return url