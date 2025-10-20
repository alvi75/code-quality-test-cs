def _verify(iface, candidate, tentative=False, vtype=None):
	"""
	Verify that *candidate* might correctly provide *iface*.

This involves:

- Making sure the candidate claims that it provides the
  interface using ``iface.providedBy`` (unless *tentative* is `True`,
  in which case this step is skipped). This means that the candidate's class
  declares that it `implements <zope.interface.implementer>` the interface,
  or the candidate itself declares that it `provides <zope.interface.provider>`
  the interface

- Making sure the candidate defines all the necessary methods

- Making sure the methods have the correct signature (to the
  extent possible)

- Making sure the candidate defines all the necessary attributes

:return bool: Returns a true value if everything that could be
   checked passed.
:raises zope.interface.Invalid: If any of the previous
   conditions does not hold.

.. versionchanged:: 5.0
    If multiple methods or attributes are invalid, all such errors
    are collected and reported. Previously, only the first error was reported.
    As a special case, if only one such error is present, it is raised
    alone, like before.
	"""
	ifv = iface.version
	if tentative:
		# We don't want to check for deprecated methods here, since we
		# already know they're there.
		for method in iface.methods:
			if method.deprecated:
				raise Invalid(
					"Method %r is deprecated; use %r instead" %
					(method, method.deprecated))
		for attr in iface.attributes:
			if attr.deprecated:
				raise Invalid(
					"Attribute %r is deprecated; use %r instead" %
					(attr, attr.deprecated))

	# Make sure the candidate implements the interface
	if iface.providedBy(candidate):
		pass
	elif iface.providedBy(candidate.__class__):
		# The candidate is a subclass of the interface
		pass
	else:
		raise Invalid("Candidate does not implement the interface")

	# Make sure the candidate provides the interface
	if iface.provides(candidate):
		pass
	elif iface.provides(candidate.__class__):
		# The candidate is a subclass of the interface
		pass
	else:
		raise Invalid("Candidate does not provide the interface")

	# Make sure the candidate has all the necessary methods
	for method in iface.methods:
		if method not in candidate.methods: