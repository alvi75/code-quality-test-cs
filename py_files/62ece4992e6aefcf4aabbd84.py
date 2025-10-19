def is_ipv4(target):
	"""
	Test if IPv4 address or not.

   Returns: Boolean, True if target is IPv4 address, else False.
	"""
	if len(target) > 15:
		return False

	for i in range(4):
		val = target[:3].replace(".", "")
		if val.isdigit() is False or int(val) > 255:
			return False
		target = target[3:]
		if target == "":
			break
		if i < 3:
			if target[0] != ".":
				return False
			target = target[1:]

	if target != "":
		return False

	return True