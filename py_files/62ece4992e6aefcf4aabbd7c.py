def oneline(script, seperator=" && "):
	"""
	Convert a script to one line command with the given seperator.

        Args:
                script: str
                separator: str
        Returns:
                str, the one-line command.
	"""
	lines = []
	for line in script.splitlines():
		if not line.strip():
			continue
		lines.append(line)
	return seperator.join(lines)