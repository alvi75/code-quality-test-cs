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
	if iface.providedBy(candidate) != tentative:
		raise Invalid("The candidate %r does not claim to provide %s" % (
			candidate, iface))
	methods = iface.getAdapterMethodNames()
	for method in methods:
		try:
			getattr(candidate, method)
		except AttributeError as e:
			raise Invalid(
				"The candidate %r does not define the method %s" % (
					candidate, method)) from e
		else:
			signature = getSignature(method, candidate)
			if not signature.isCompatibleWith(iface.getAdapterMethodSignature(method)):
				raise Invalid(
					"The method %s of the candidate %r has the wrong signature"
					% (method, candidate))

	attributes = iface.getAdapterAttributeNames()
	for attribute in attributes:
		try:
			getattr(candidate, attribute)
		except AttributeError as e:
			raise Invalid(
				"The candidate %r does not define the attribute %s" % (
					candidate, attribute)) from e
		else:
			value = getattr(candidate, attribute)
			if not isinstance(value, iface.getAdapterAttributeType(attribute)):
				raise Invalid(
					"The attribute %s of the candidate %r has the wrong type"
					% (attribute, candidate))