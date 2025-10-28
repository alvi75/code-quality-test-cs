def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if isinstance(target, str):
		try:
			socket.inet_pton(socket.AF_INET, target)
			return True
		except socket.error:
			pass

	return False