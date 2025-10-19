def parser_flags(parser):
		"""
		Given an argparse.ArgumentParser instance, return its argument flags in a space-separated string.
    Args:
        script: argparse.ArgumentParser instance

    Returns:
        argument flags in a space-separated string
	"""
	parser = parser._get_positionals()
	flags = []
	for arg in parser._actions:
		if isinstance(arg, argparse.ArgumentAction) and arg.dest is not None:
			flag = "--" + arg.dest.replace('_', '-')
			if flag not in flags:
				flags.append(flag)
	return ' '.join(flags)