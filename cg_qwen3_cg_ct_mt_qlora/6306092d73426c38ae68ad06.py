def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silent_args = []
	for arg in args:
		if arg.startswith('-'):
			arg = arg[1:]
			if arg in self.silent_args:
				silent_args.append(arg)
	return silent_args