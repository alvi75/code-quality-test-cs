def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	if isinstance(host, str) and host in ['localhost', '127.0.0.1']:
		return True
	elif isinstance(host, int) and host == 127:
		return True
	else:
		return False