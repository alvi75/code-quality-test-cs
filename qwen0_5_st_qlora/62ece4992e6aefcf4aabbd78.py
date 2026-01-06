def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	if not isinstance(host, str):
		return False
	if host == 'localhost':
		return True
	if host in ['127.0.0.1', '::1']:
		return True
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', host):
		return True
	return False