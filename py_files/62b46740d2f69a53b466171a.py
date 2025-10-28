def pretty(self, indent=0, debug=False):
	"""
	Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	"""
	debug_details = ""
	if debug:
		debug_details += ", debug: True"
	obj = None
	if isinstance(self.obj, str):
		obj = f"'{self.obj}'"
	else:
		obj = repr(self.obj)
	return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"