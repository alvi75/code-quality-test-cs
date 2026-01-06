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
		host = str(host)

	if host == 'localhost' or host == '127.0.0.1':
		return True

	try:
		ipaddress.ip_address(host)
	except ValueError:
		pass
	else:
		return True

	user_name = os.environ.get('USER', '')
	local_domain_name = socket.getfqdn().split('.')[0]
	domain_name = socket.getfqdn()
	hostname = socket.gethostname()

	if (host == user_name) or (host == local_domain_name) or (host == domain_name) or (host == hostname):
		return True

	return False