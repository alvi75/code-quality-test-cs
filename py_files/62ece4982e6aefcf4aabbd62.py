def _replace_url_args(url, url_args):
    """
	Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
	"""
    if not isinstance(url_args, dict) or len(url_args) == 0:
        return url

    # Get the scheme, netloc, path, query, frag
    scheme, netloc, path, query, frag = urllib.parse.urlsplit(url)

    # Replace the parameters
    for k, v in url_args.items():
        if k in query:
            query = query.replace(k, str(v))
        elif k in frag:
            frag = frag.replace(k, str(v))

    return urllib.parse.urlunsplit((scheme, netloc, path, query, frag))