def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string
	"""
	flags = []
	for action in parser._actions:
		if not isinstance(action, _SubParsersAction) or action.dest == 'subparser':
			continue
		flags.append(action.dest)
	return ' '.join(flags)