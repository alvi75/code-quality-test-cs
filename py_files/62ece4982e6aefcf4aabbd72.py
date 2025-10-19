def unquote(name):
    """
	Remove quote from the given name with regular expression.
    Args:
        name: input name
    Returns:
        name after removal
	"""
    if not isinstance(name, six.string_types):
        return name

    # remove quotes
    name = re.sub(r"^['\"]|['\"]$", '', name)
    return name