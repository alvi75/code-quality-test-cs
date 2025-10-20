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
		raise Invalid("The candidate %r does not claim to provide %r" %
			(candidate, iface))
	
	errors = []
	for method_name in iface['methods']:
		try:
			method = getattr(candidate, method_name)
		except AttributeError:
			errors.append(Invalid(
				"The candidate %r does not define the method %r" %
				(candidate, method_name)))
		else:
			signature = inspect.signature(method)
			required_args = set(signature.parameters.keys())
			if required_args - iface['method'][method_name]['args']:
				errors.append(Invalid(
					"The method %r of the candidate %r has too few arguments"
					% (method_name, candidate)))
			elif required_args > iface['method'][method_name]['args']:
				errors.append(Invalid(
					"The method %r of the candidate %r has too many arguments"
					% (method_name, candidate)))

	for attr_name in iface['attributes']:
		try:
			attr = getattr(candidate, attr_name)
		except AttributeError:
			errors.append(Invalid(
				"The candidate %r does not define the attribute %r" %
				(candidate, attr_name)))
		else:
			if