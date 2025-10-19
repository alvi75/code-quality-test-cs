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
	if iface.providedBy(candidate) or tentative:
		pass
	else:
		raise Invalid("%r does not provide %r" % (candidate, iface))

	def check(method, name, required, msg):
		if method is None:
			return False
		sig = signature(method)
		if len(required) > 1:
			sig_args = sig.parameters.keys()
		elif len(required) == 1:
			sig_args = [required[0]]
		else:
			sig_args = []
		if sig_args != required:
			if vtype is None:
				raise Invalid(msg)
			else:
				vtype.append(msg)

		return True

	def check_attr(attr, name, required, msg):
		if attr is None:
			return False
		val = getattr(candidate, attr)
		if val is None:
			if vtype is None:
				raise Invalid(msg)
			else:
				vtype.append(msg)
		return True

	def check_methods(iface, candidate, names, msg):
		for name in names:
			methods = [
				getattr(candidate.__class__, name, None),
				getattr(candidate, name, None),
			]
			if not any(check(m, name, iface._methods[name], msg) for