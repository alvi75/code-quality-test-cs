def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
	string.
	"""
	flags = [ ]
	for arg in parser._actions:
		if arg.dest == 'flags':
			flags.extend(arg.values)
	return ' '.join(flags)