def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	return ' '.join(
		'--' + flag for flag in parser._option_string_actions.keys()
	)