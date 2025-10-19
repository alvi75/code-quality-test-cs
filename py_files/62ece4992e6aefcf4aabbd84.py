def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if isinstance(target, str) and re.match(r'^(\d{1,3}\.){3}(\d{1,3})$', target):
		return True
	elif isinstance(target, tuple) and len(target) == 4:
		for i in range(0, 4):
			if (target[i] < 0 or target[i] > 255):
				return False
		return True
	else:
		return False