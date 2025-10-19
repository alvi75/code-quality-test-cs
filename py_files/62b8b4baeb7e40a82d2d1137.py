def verifyObject(iface, candidate, tentative=False):
	"""
	Verify that *candidate* might correctly provide *iface*.

This involves:

- Making sure the candidate claims that it provides the
  interface using ``iface.providedBy`` (unless *tentative* is `True`),
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
    As a special case, if multiple such error are present, it is raised
    alone, like before.
	"""
	if iface is None:
		return True
	if candidate is None:
		return False
	if isinstance(candidate, type) and issubclass(candidate, BaseClass):
		candidate = candidate()
	if not hasattr(candidate, "provides"):
		raise Invalid("%s doesn't provide %r" % (candidate, iface))
	if iface.providedBy(candidate):
		return True
	if not iface.implements:
		raise Invalid("interface '%s' must declare 'implements' to "
			"specify what it implements" % iface)
	if iface.implements != iface.__class__:
		raise Invalid("interface '%s' cannot implement both "
			"'%s' and '%s'" % (
				iface.implements, iface.__class__,
				iface.providedBy))
	if iface.implements == iface:
		raise Invalid("interface '%s' cannot implement itself" % iface)
	if iface.implements in _already_provided:
		return True
	if iface.implements in _already_declared:
		return True
	if iface.implements in _already_defined:
		return True
	if iface.implements in _already_called:
		return True
	if iface.implements in _already_tentative:
		return True
	if iface.implements in _already_declared: