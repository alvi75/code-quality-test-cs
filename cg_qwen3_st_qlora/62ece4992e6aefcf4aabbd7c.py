def oneline(script, seperator=" && "):
	"""
	Convert a script to one line command with the given seperator.

        Args:
                script: str
                separator: str
        Returns:
                str, the one-line command.
	"""
	if not isinstance(script, str):
		raise TypeError("script must be string")
	if not isinstance(seperator, str):
		raise TypeError("seperator must be string")

	return seperator.join(script.splitlines())