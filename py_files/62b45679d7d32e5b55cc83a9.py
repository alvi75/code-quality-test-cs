def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	return ' '.join(
		arg.split('=')[0] for arg in parser.format_help().split()
		if arg.startswith('-')
	)