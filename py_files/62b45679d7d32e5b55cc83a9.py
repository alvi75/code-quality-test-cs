def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
	string.
	"""
	flags = []
	for arg in parser._actions:
		if isinstance(arg, argparse.Action):
			flags.append(arg.dest)
	return ' '.join(flags)