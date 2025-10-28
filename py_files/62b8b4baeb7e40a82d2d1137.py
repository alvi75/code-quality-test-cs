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

	if not isinstance(candidate, type) and not hasattr(candidate, 'providedBy'):
		raise TypeError("verifyObject() requires a class or object")

	if tentative:
		return True

	if not iface.providedBy(candidate):
		return False

	for name, method in inspect.getmembers(candidate, predicate=inspect.ismethod):
		try:
			method.__providable__ = True
		except AttributeError:
			pass

		if not method.__providable__:
			continue

		if not method.__providable__(iface):
			return False

		if not _is_method_valid(method, iface):
			return False

		if not _is_method_signature_valid(method, iface):
			return False

		if not _is_method_attributes_valid(method, iface):
			return False

		if not _is_method_docstring_valid(method, iface):
			return False

		if not _is_method_annotations_valid(method, iface):
			return False

		if not _is_method_typehints_valid(method, iface):
			return False

		if not _is_method_overloads_valid(method, iface):
			return False

		if not _is_method_overload_names_valid(method, iface):
			return False

		if not _is_method_overload_args_valid(method, iface):
			return False