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
	if not tentative:
		if not iface.providedBy(candidate):
			raise Invalid("Candidate does not provide interface",
						   candidate, iface)
	for method in iface.names():
		if method not in candidate.__dict__:
			raise Invalid("Candidate does not define method",
						   candidate, iface, method)
		if vtype is not None:
			if not isinstance(candidate.__dict__[method], vtype):
				raise Invalid("Method is not of correct type",
							   candidate, iface, method)
	for attr in iface.names(True):
		if attr not in candidate.__dict__:
			raise Invalid("Candidate does not define attribute",