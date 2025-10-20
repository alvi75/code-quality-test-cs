def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""

	if len(target) != 4:
		return False

	for i in range(0, 4):
		try:
			target[i] = int(target[i])
		except ValueError:
			return False

		if target[i] < 0 or target[i] > 255:
			return False

	return True