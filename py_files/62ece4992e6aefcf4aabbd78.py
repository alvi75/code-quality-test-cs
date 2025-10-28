def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""

	if not isinstance(host, basestring):
		host = str(host)

	return (host == 'localhost' or
			host == socket.gethostname() or
			host == socket.getfqdn() or
			host == '127.0.0.1')