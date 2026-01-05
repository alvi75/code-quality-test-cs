def verifyClass(iface, candidate, tentative=False):
	"""
	Verify that the *candidate* might correctly provide *iface*.
	"""
	if not iface:
		raise ValueError("No interface specified")
	if not candidate:
		raise ValueError("No candidate specified")

	# Check if the candidate is a subclass of iface
	if not isinstance(candidate, iface):
		raise TypeError("Candidate must be a subclass of %s" % iface)

	# Check if the candidate provides the interface
	for method in iface.methods():
		if not hasattr(candidate, method):
			raise AttributeError("Candidate does not provide method '%s'" % method)

	# Check if the candidate implements the interface
	for method in iface.interfaces():
		if not hasattr(candidate, method):
			raise AttributeError("Candidate does not implement interface '%s'" % method)

	# Check if the candidate implements the interface
	for method in iface.methods():
		if not hasattr(candidate, method):
			raise AttributeError("Candidate does not provide method '%s'" % method)

	# Check if the candidate implements the interface
	for method in iface.interfaces():
		if not hasattr(candidate, method):
			raise AttributeError("Candidate does not implement interface '%s'" % method)