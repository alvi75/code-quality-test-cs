def is_local(host):
		"""
		Checks if the host is the localhost,
    the localhost include local IP, user name, local domain name, `localhost` and `127.0.0.1`

    Args:
        host: The hostname or ip

    Returns:
        True if the host is the localhost else False
	"""

	# Check for a valid IP address
	if re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', host):
		return True

	# Check for a valid hostname
	if re.match(r'^[a-zA-Z0-9._-]+$', host):
		return True

	# Check for a valid hostname with a domain part
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+$', host):
		return True

	# Check for a valid hostname with a domain part and a port number
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+:[0-9]{1,5}$', host):
		return True

	# Check for a valid hostname with a domain part and a port number and a protocol
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+:[0-9]{1,5}([/]?[a-zA-Z0-9.-]+)$', host):
		return True

	# Check for a valid hostname with a domain part and a port number and a protocol and a username
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+:[0-9]{1,5}([/]?[a-zA-Z0-9.-]+)@$', host):
		return True

	# Check for a valid hostname with a domain part and a port number and a protocol and a password
	if re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+:[0-9]{1,5}([/]?[a-zA-Z0-9.-]+):[a-zA-Z0-9.-]+$', host):
		return True

	# Check for a valid hostname with a domain part and a port number and a protocol and a password and a username
	if re.match