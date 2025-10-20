def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string
	"""
	return ' '.join([arg for arg in parser._actions if isinstance(arg, Argument) or isinstance(arg, NamespaceAction)])