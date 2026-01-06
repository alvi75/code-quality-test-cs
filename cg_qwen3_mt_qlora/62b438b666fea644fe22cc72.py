def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = []
	for action in parser._actions:
		if not action.option_strings:
			continue
		flags.extend(action.option_strings)
	return ' '.join(flags)