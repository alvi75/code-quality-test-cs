def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	if host in ['localhost', '127.0.0.1']:
		return True
	elif host == get_ip():
		return True
	elif host == get_user_name():
		return True
	elif host == get_domain_name():
		return True
	else:
		return False