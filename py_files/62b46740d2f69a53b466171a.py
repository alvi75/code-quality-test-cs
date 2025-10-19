def pretty(self, indent=0, debug=False):
	"""
	Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	"""
	if not isinstance(self.obj, str):
		return (f"{indent*' '}{self.__class__.__name__}({self.debug_details}) {self.obj}")  # TODO: add more details to this message
	else:
		return (f"{indent*' '}{self.__class__.__name__}({self.debug_details}{self.obj})")