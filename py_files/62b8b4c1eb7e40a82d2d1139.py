def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isinstance(candidate, type) or not issubclass(candidate, object):
		return False

	for base in candidate.__bases__:
		if base == object:
			continue
		if verifyClass(iface, base, tentative=True):
			break
	else:
		return False

	if tentative:
		return True

	try:
		candidate.im_class_getattr
	except AttributeError:
		pass
	else:
		return True

	try:
		candidate.__getattribute__
	except AttributeError:
		pass
	else:
		return True

	return False