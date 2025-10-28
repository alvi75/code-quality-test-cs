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

	iface = iface._getImplementation()
	candidate = candidate._getImplementation()

	methods = iface.methods
	attributes = iface.attributes

	# Make sure the candidate implements the interface
	if iface.implements:
		for method in iface.implements:
			try:
				method(self)
			except AttributeError as e:
				raise Invalid("Candidate %r does not implement %r" %
				               (candidate, iface), e)

	# Make sure the candidate provides the interface
	if iface.provides:
		for attribute in iface.provides:
			try:
				attribute(candidate)
			except AttributeError as e:
				raise Invalid("Candidate %r does not provide %r" %
				               (candidate, iface), e)

	# Make sure the candidate has all the required methods
	for method in methods:
		try:
			method(candidate)
		except AttributeError as e:
			raise Invalid("Candidate %r does not provide %r" %
			               (candidate, method), e)

	# Make sure the candidate has all the required attributes
	for attribute in attributes:
		try:
			attribute(candidate)
		except AttributeError as e:
			raise Invalid("Candidate %r does not define %r" %
			               (candidate, attribute), e)

	return True