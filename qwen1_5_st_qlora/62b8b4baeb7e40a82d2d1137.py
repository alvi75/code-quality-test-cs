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
		if iface.providedBy(candidate) is False:
			raise Invalid("Candidate %s does not claim to implement %r" %
			              (candidate.__class__.__name__, iface))
	except AttributeError:
		pass

	for name, method in inspect.getmembers(candidate, predicate=inspect.ismethod):
		method = getattr(method, '__func__', method)
		if not hasattr(method, 'im_func'):
			continue
		if not isinstance(method.im_func, types.MethodType):
			continue
		if not hasattr(method.im_func, '__self__'):
			continue
		if not hasattr(method.im_func.__self__, '__class__'):
			continue
		if not hasattr(method.im_func.__self__, '__dict__'):
			continue
		if not hasattr(method.im_func.__self__.__dict__, '__getitem__'):
			continue
		if not hasattr(method.im_func.__self__.__dict__, '__contains__'):
			continue
		if not hasattr(method.im_func.__self__.__dict__, '__iter__'):
			continue
		if not hasattr(method.im_func.__self__.__dict__, '__len__'):
			continue
		if not hasattr(method.im_func.__self__.__dict__, '__getitem__'):
			continue
		if not hasattr(method.im_func.__self