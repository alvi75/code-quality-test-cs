def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not isInterface(iface):
		raise TypeError("First argument must be a zope.interface.Interface")
	if not isclass(candidate) or not issubclass(candidate, object):
		raise TypeError("Second argument must be a class")

	# If we're in a tentatively-registered state, then we don't need to
	# check for the interface; it's already registered.
	if tentative:
		return

	# Check if the candidate implements the interface.
	try:
		candidate.providedBy(iface)
	except AttributeError:
		pass
	else:
		return

	# Check if the candidate provides the interface.
	try:
		candidate.implements(iface)
	except AttributeError:
		pass
	else:
		return

	# Check if the candidate is a subclass of the interface.
	try:
		isinstance(candidate, iface)
	except TypeError:
		pass
	else:
		return

	# Check if the candidate is a subclass of the interface's base classes.
	for base in iface.__bases__:
		try:
			isinstance(candidate, base)
		except TypeError:
			pass
		else:
			return

	# Check if the candidate is a subclass of the interface's direct bases.
	for base in iface.getDirectBaseClasses():
		try:
			isinstance(candidate, base)
		except TypeError:
			pass
		else:
			return

	# Check if the candidate is a subclass of the interface's direct bases,
	# but only if they are interfaces.
	for base in iface.getDirectBaseInterfaces():
		try:
			isinstance(candidate, base)
		except TypeError:
			pass
		else:
			return

	# Check if the candidate is a subclass of the interface's direct bases,
	# but only if they are interfaces, and they are not abstract.
	for base in iface.getDirectBaseInterfaces():
		try:
			isinstance(candidate, base)
		except TypeError:
			pass
		else:
			if not base.isAbstract():
				return

	# Check if the candidate is a subclass of the interface's direct bases,
	# but only if they are interfaces, and they are not abstract, and they
	# have no abstract methods.
	for base in iface.getDirectBaseInterfaces():
		try:
			isinstance(candidate, base)
		except TypeError:
			pass
		else:
			if not base.isAbstract() and not base.has