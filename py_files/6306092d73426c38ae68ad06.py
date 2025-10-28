def get_silent_args(self, args):
	"""
	list of silenced argument

:param args: The received arguments.
:return: list, slienced argument names
	"""
	silence = self.get_silence()
	if silence:
		return [arg for arg in args if arg not in silence]
	else:
		return []