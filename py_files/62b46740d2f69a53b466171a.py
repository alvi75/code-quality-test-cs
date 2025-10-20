def pretty(self, indent=0, debug=False):
	"""Return a pretty formatted representation of self. obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"
	"""
	debug_details = ""
	if debug:
		debug_details += "\n"
		for key in sorted(self.debug.keys()):
			value = self.debug[key]
			debug_details += f"\t{key}: {value}\n"

	obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
	return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"