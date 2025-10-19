def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
		return [os.path.realpath(os.path.expanduser(c)) for c in cmd]