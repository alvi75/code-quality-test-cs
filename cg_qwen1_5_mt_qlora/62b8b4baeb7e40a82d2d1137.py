def verifyObject(iface, candidate, tentative=False):
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

	try:
		candidate_provides = iface.providedBy(candidate)
	except AttributeError as e:
		raise Invalid("Candidate %s does not implement %s" % (candidate.__name__, iface))

	if not candidate_provides:
		raise Invalid("Candidate %s does not claim to provide %s" % (candidate.__name__, iface))

	for method_name in iface.methods():
		method = getattr(iface, method_name)
		if not hasattr(candidate, method_name) and not tentative:
			raise Invalid("Candidate %s does not define method '%s'" % (candidate.__name__, method_name))
		elif not callable(getattr(candidate, method_name)) and not tentative:
			raise Invalid("Candidate %s does not define callable method '%s'" % (candidate.__name__, method_name))

		try:
			argspec = inspect.getargspec(method)
		except TypeError:
			pass
		else:
			if argspec.varargs or argspec.keywords:
				continue

			if len(argspec.args) == 1 and argspec.args[0] == 'self':
				continue

			if argspec.args:
				if argspec.args[0] != 'self' and argspec.args[0] != 'cls':
					continue