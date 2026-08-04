def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	return ' '.join(
		'--' + flag for flag in parser._get_option_tuples()
		if flag[0] not in ('-h', '--help')
	)