def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silent = []
	for arg in args:
		if self.silent_arg_re.match(arg):
			silent.append(arg)
	return silent