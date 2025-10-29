def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silent = []
	for arg in args:
		if self.is_silence(arg):
			silent.append(arg)
	return silent