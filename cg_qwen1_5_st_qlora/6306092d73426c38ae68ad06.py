def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silence = []
	for arg in self.silenced:
		if arg in args:
			silence.append(arg)
	return silence