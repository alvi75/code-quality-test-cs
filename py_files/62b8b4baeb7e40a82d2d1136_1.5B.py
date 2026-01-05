def _verify(iface, candidate, tentative=False, vtype=None):
	"""Verify that *candidate* might correctly provide *iface*.

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

	if tentative:
		return True

	def verify_method(method_name):
		method = getattr(candidate, method_name)
		if not hasattr(method, 'im_func'):
			raise Invalid("Method %s has no __func__ attribute" % method_name)
		if not isinstance(method.im_func, types.MethodType):
			raise Invalid("%s.%s is not a method" % (candidate.__name__, method_name))
		if not hasattr(method, 'im_class') or not method.im_class == iface:
			raise Invalid("%s.%s is not implemented by %s" % (candidate.__name__, method_name, iface))

		try:
			argspec = inspect.getargspec(method.im_func)
		except TypeError as e:
			raise Invalid(str(e))

		if argspec.varargs or argspec.keywords:
			raise Invalid("%s.%s has variable arguments" % (candidate.__name__, method_name))

		for arg in argspec.args:
			if arg.startswith('_'):
				continue
			if not hasattr(method, arg) or not hasattr(getattr(method, arg), '__call__'):
				raise Invalid("%s.%s requires argument '%s'" % (candidate.__name__, method_name, arg))

		if not hasattr(method, 'im_self'):
			raise