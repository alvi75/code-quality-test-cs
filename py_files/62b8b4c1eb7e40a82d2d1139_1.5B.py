def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""

	if not isInterface(iface) or not isClass(candidate):
		return False

	for i in iface.__bases__:
		if i == object:
			break
		elif i in candidate.__bases__:
			continue
		else:
			return False

	if tentative:
		return True

	try:
		candidate()
	except TypeError as e:
		return False

	return True