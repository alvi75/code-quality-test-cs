def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silence = []
	for arg in self.args:
		if not getattr(arg, 'silence', False):
			continue
		if isinstance(getattr(arg, 'default'), bool) or \
				getattr(arg, 'type', None) is str:
			continue
		silence.append(arg.name)
	return silence