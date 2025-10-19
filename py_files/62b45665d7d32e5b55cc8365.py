def parse_arguments(*unparsed_arguments):
		"""
		Parses parameters and returns them as dict maps
		"""
		parser = argparse.ArgumentParser()
		subparsers = parser.add_subparsers()

		for name, description in arguments.items():
			parsed_args = subparsers.add_parser(name)
			parsed_args.description = description

			for argname, argtype in args.items():
				if isinstance(argtype, list):
					parsed_args.add_argument('--' + argname, nargs='+', type=argtype[0],
						help=' '.join([argname, ' '.join(argtype[1:])]))
				else:
					parsed_args.add_argument('--' + argname, type=argtype,
						help=' '.join([argname, str(argtype)]))

			args[name] = parsed_args.parse_args(unparsed_arguments)

		return args