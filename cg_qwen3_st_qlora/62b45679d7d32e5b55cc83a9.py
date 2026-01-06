def parser_flags(parser):
	"""
	Given an argparse.ArgumentParser instance, return its argument flags in a space-separated
string.
	"""
	flags = []
	for action in parser._actions:
		if isinstance(action, argparse._SubParsersAction):
			flags.append('subparser')
		elif isinstance(action, argparse.Action):
			flags.append(action.dest)
	return ' '.join(flags)