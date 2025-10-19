def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
	string.
	"""
	return ' '.join([f[1:] for f in parser._actions if f.startswith('-')])