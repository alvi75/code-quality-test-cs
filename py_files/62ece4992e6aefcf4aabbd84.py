def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""

	if isinstance(target, str) and re.match(r'^\d+\.\d+\.\d+\.\d+$', target):
		return True

	return False