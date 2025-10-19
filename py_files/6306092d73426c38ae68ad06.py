def get_silent_args(self, args):
		"""
		def get_silent_args(self, args):
		The received arguments.
		:return: list, slienced argument names
		"""
		silent = []
		for arg in args:
			if self.silent_arg.match(arg) is not None:
				silent.append(arg)
		return silent