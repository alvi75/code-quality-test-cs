def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not hasattr(self, '__dict__'):
		return []
	names = [name for name in dir(self) if not name.startswith('__')]
	if all:
		return names
	else:
		return [name for name in names if not name[0].isdigit()]