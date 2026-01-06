def oneline(script, seperator=" && "):
	"""
	Convert a script to one line command with the given seperator.

        Args:
                script: str
                separator: str
        Returns:
                str, the one-line command.
	"""
	return seperator.join([line for line in script.splitlines() if not line.startswith("#")])