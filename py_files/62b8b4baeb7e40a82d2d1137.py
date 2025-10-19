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

	if not isinstance(iface, Interface) and not isclass(iface):
		raise Invalid("interface must be a string or Interface object")

	if iface.providedBy:
		candidate_provides = getattr(candidate, "providedBy", None)
		if candidate_provides is None:
			raise Invalid(
				"object %r has no attribute 'providedBy'" % candidate
			)
		elif not isinstance(candidate_provides, list):
			raise Invalid(
				"object %r providedBy attribute is not a list" % candidate
			)
		else:
			for prov in candidate_provides:
				if not isinstance(prov, Interface):
					raise Invalid(
						"object %r providedBy element is not an Interface"
						% prov
					)
				elif not prov.providedBy:
					raise Invalid(
						"object %r providedBy element is empty" % prov
					)
				elif not iface.providedBy(prov):
					raise Invalid(
						"object %r providedBy element does not implement %s"
						% (prov, iface)
					)

		candidate_implements = getattr(candidate, "implements", None)
		if candidate_implements is None:
			raise Invalid(
				"object