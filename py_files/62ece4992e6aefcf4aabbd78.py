def is_local(host):
	"""
	Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""
	if host == "localhost" or (host.find(":") != -1 and host.split(":")[0] == "127"):
		return True
	elif re.match(r"(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:[a-z]{2,6}\.?|[a-z0-9-]{2,}\.?)|(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?|(?:[a-z0-9-]{2,63}(?<!-)\.?(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?))?(?:\.(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+)*$)", host) is not None:
		return True
	else:
		return False