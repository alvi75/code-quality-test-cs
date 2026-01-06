def pretty(self, indent=0, debug=False):
	"""
	Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	"""
	if not self._pretty:
		self._pretty = True
		return (indent + 1) * ' ' + f"{self.__class__.__name__}({debug_details}{repr(self.obj)})"

	def __str__(self):
		return self.pretty(debug=True)

	def __repr__(self):
		return self.pretty(debug=True)