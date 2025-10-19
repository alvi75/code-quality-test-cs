def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string
	"""
	args = []
	for action in parser._actions:
		if not hasattr(action, 'option_strings'):
			continue
		for option_string in action.option_strings:
			args.append(option_string)
	return " ".join(args)