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
	if not isinstance(candidate, type) and not hasattr(candidate, 'providedBy'):
		raise TypeError("The provided object %r is neither a type nor "
						"has a providedBy attribute." % candidate)
	if not iface:
		return True
	if tentative:
		if not candidate.providedBy(iface):
			return False
	else:
		if not candidate.providedBy(iface):
			return False
	# Check for missing methods
	for method_name in iface._methods:
		method = getattr(iface, method_name)
		try:
			candidate_method = getattr(candidate, method_name)
		except AttributeError:
			# The candidate doesn't define the method
			continue
		if not callable(candidate_method):
			# The candidate defines something other than a function
			continue
		if not method.im_func.__code__.co_argcount == \
				candidate_method.im_func.__code__.co_argcount:
			# The number of arguments differs
			continue
		if not method.im_func.__code__.co_varnames[:method.im_func.__code__.co_argcount] == \
				candidate_method.im_func.__code__.co_varnames[:method.im_func.__code__.co_argcount]:
			# The argument names