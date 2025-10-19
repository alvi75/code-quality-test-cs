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
    As a special case, if multiple such errors are present, it is raised
    alone, like before.
	"""
	if iface is None:
		return False

	if vtype is None:
		vtype = iface.vartype

	if iface.isAbstract():
		raise Invalid("abstract interfaces cannot be implemented",
			argument="interface", iface=iface)
	if iface.isInterface() and iface.isAbstract():
		raise Invalid("interfaces may not implement abstract interfaces",
			argument="interface", iface=iface)

	if iface.isClass():
		if iface.name == "object":
			raise Invalid("classes may not provide 'object' interface",
				argument="interface", iface=iface)
		if iface.name != "object" and iface.superClasses:
			raise Invalid("class '%s' should not declare its own super classes"
				% iface.name, argument="super classes", iface=iface)
		if iface.name == "object" and iface.superClasses:
			raise Invalid("class '%s' should not inherit from its own super classes"
				% iface.name, argument="super classes", iface=iface)

	if iface.name == "object" and iface.superClasses:
		raise Invalid("class '%s' should not inherit from its own super classes"
			% iface.name, argument="super classes", iface=iface)

	if iface.name == "object" and