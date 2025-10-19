def _make_glob_path(path):
		if os.path.isfile(path) or os.path.islink(path):
			return path
		else:
			return os.path.join(path, '*')

	return tuple(_make_glob_path(p) for p in find_paths)