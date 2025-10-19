def _parse_args(args):
		parser = argparse.ArgumentParser()
		for arg in args:
			if not isinstance(arg, str):
				raise TypeError("Argument must be a string")
			elif arg.startswith("-"):
				arg = arg[1:]
			else:
				arg = "--" + arg

			if arg == "help":
				return parser.parse_args(["-h"])
			elif arg == "version":
				return parser.parse_args(["-v"])

			groups = arg.split("=")
			if len(groups) > 1:
				key = groups[0]
				value = groups[1]

				if key == "verbose":
					parser.add_argument("--verbose", action="store_true")
				elif key == "debug":
					parser.add_argument("--debug", action="store_true")
				elif key == "log_file":
					parser.add_argument("--log-file", type=str, default=None)
				elif key == "log_level":
					parser.add_argument("--log-level", type=int, default=20)
				elif key == "log_format":
					parser.add_argument("--log-format", type=str, default="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
				elif key == "log_datefmt":
					parser.add_argument("--log-datefmt", type=str, default="%Y-%m-%d %H:%M:%S")
				elif key == "log_timeformat":
					parser.add_argument("--log-timeformat", type=str, default="%I:%M:%S")
				elif key == "log_msec":
					parser.add_argument("--log-msec", type=int, default=3)
				elif key == "log_msec_format":
					parser.add_argument("--log-msec-format", type=str, default="%03d")
				elif key == "log_msec_timeformat":
					parser.add_argument("--log-msec-timeformat", type=str, default="%I:%M:%S.%f")
				elif key == "log_msec_timeformat":
					parser.add_argument("--log-msec-timeformat", type=str, default="%I:%M:%S.%f")
				elif key == "log_msec_timeformat":
					parser.add_argument("--log-msec-timeformat", type=str, default="%I:%M:%S.%f")
				elif key == "log_msec_timeformat":
					parser.add_argument("--log-msec-timeformat", type=str, default="%I:%M:%S.%f")
				elif key == "log_msec_timeformat