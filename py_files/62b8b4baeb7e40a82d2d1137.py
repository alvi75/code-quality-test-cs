def verifyObject(iface, candidate, tentative=False):
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
	if iface.providedBy(candidate) != True:
		raise Invalid("%r does not declare to provide %r" % (
			candidate, iface))
	def check(name, predicate, msg=None):
		if not predicate():
			if msg is None:
				msg = "%r missing" % name
			raise Invalid(msg)
	for method in iface._methods:
		check(method.__name__, lambda: method in candidate)
		methods = getattr(candidate, method.__name__)
		if isinstance(methods, tuple):
			sig = _signature(method)
			for i, (arg, type_) in enumerate(sig.parameters.items()):
				if arg == "self":
					continue
				try:
					value = methods[i]
				except IndexError:
					if tentative:
						break
					else:
						raise
				if not type_.check(value):
					if tentative:
						break
					else:
						raise Invalid(
							"Wrong parameter type for %r at index %d"
							% (method, i))
	for attr in iface._attributes:
		check(attr, lambda: attr in candidate)
		attribs = getattr(candidate, attr)
		if isinstance(attribs, tuple):
			for value in attribs:
				if not iface._attributes[attr].check(value):