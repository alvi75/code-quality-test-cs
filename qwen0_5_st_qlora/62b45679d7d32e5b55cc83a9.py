def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
	string.
	"""
	flags = []
	for arg in parser._get_allowed_names():
		if arg not in parser._mutually_exclusive_groups:
			flags.append(arg)
	return ' '.join(flags)