def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""

	silent_args = []
	for arg in self.silent:
		if arg in args:
			silent_args.append(arg)
	return silent_args