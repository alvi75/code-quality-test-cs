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
		if isinstance(action, argparse._SubParsersAction):
			for subparser in action.choices.values():
				flags.extend(parser_flags(subparser))
		elif not isinstance(action, argparse._StoreAction):
			flags.append(action.dest)
	return ' '.join(flags)