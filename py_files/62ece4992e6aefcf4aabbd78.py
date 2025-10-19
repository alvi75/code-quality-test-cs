def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	try:
		# Check if the host is a valid IP address
		if not net_utils.is_valid_ipv4(host) and not net_utils.is_valid_ipv6(host):
			host = socket.gethostbyname(host)
	except Exception as e:
		return False
	if host in ['127.0.0.1', '::1']:
		return True
	if os.name == 'nt':
		if host.lower() in get_localhost_name():
			return True
	else:
		if host in [socket.gethostname(), socket.getfqdn()]:
			return True
	return False