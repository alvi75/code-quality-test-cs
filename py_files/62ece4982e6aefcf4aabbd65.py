def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string
	"""
	flags = ""
	for arg in parser._get_positional_args():
		if flags == "":
			flags += arg
		else:
			flags += " %s" % arg
	return flags