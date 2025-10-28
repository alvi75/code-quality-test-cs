def determineMetaclass(bases, explicit_mc=None):
	"""
	Determine metaclass from 1+ bases and optional explicit __metaclass__
	"""
	if not explicit_mc:
		explicit_mc = None

	for base in bases:
		if is_metaclass(base) or is_class(base):
			return base

	if explicit_mc:
		return explicit_mc

	raise MetaclassesNotDefined("No metaclass found")