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
	if iface.providedBy(candidate) != tentative:
		raise Invalid("The candidate %r does not claim to provide %s" % (
			candidate, iface))
	methods = iface.getAdapterMethodNames()
	for method in methods:
		try:
			meth = getattr(candidate, method)
		except AttributeError:
			raise Invalid(
				"The candidate %r does not define the method %s" % (
					candidate, method))
		else:
			if vtype is None:
				pass
			elif not isinstance(meth, vtype):
				raise Invalid(
					"The method %s of the candidate %r is not of type %s"
					% (method, candidate, vtype.__name__))
			sig = inspect.signature(meth)
			args = sig.parameters.keys()
			if args - set(methods):
				raise Invalid(
					"The method %s of the candidate %r has extra arguments "
					"that are not defined by the interface %s" %
					(method, candidate, iface))
			if set(methods) - args:
				raise Invalid(
					"The method %s of the candidate %r is missing arguments "
					"that are defined by the interface %s" %
					(method