def oneline(script, seperator=" && "):
    """
	Convert a script to one line command with the given seperator.

        Args:
                script: str
                separator: str
        Returns:
                str, the one-line command.
	"""
    if not isinstance(script, six.string_types):
        raise TypeError("script must be string")
    return seperator.join([six.text_type(x) for x in script])