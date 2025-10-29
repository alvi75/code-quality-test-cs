def _replace_url_args(url, url_args):
	"""
	Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
	if not url_args:
		return url

	url = urlparse.urlsplit(url)
	for key, value in url_args.items():
		if key == 'url':
			continue
		if key == 'query':
			query = parse_qs(url.query)
			query[key] = [value]
			url = urlunparse((url.scheme, url.netloc, url.path, '', urlencode(query), ''))

	return url.geturl()