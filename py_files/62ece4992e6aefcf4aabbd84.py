def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', target) is not None:
		return True
	else:
		return False