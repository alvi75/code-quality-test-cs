def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if isinstance(target, str) and len(target.split('.')) == 4:
		return True
	else:
		return False