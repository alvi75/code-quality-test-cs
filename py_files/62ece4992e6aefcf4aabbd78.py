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

	return (
			is_ip(host) or
			is_user_name(host) or
			is_domain_name(host) or
			is_localhost(host)
	)