def verifyObject(iface, candidate, tentative=False):
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
	if iface is None:
		raise Invalid("iface cannot be None")
	if candidate is None:
		raise Invalid("candidate cannot be None")

	# Make sure the candidate implements the interface
	if iface.providedBy(candidate):
		pass
	elif iface.providedBy(candidate.__class__):
		# The candidate is a subclass of the interface
		pass
	else:
		raise Invalid(
			"candidate %r does not implement the interface %r"
			% (candidate, iface)
		)

	# Make sure the candidate provides the interface
	if iface.provides(candidate):
		pass
	elif iface.provides(candidate.__class__):
		# The candidate is a subclass of the interface
		pass
	else:
		raise Invalid(
			"candidate %r does not provide the interface %r"
			% (candidate, iface)
		)

	# Make sure the candidate has all the necessary methods
	for method in iface.methods:
		try:
			method(candidate)
		except AttributeError as e:
			raise Invalid(
				"candidate %r does not define the method %r"
				% (candidate, method)
			) from e

	# Make sure the candidate has all the necessary attributes
	for attribute in iface.attributes: