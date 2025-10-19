def _register_vcs_handler(method):
		if not hasattr(method, '_vcs_handlers'):
			method._vcs_handlers = {}
		method._vcs_handlers[vcs] = method

	return _register_vcs_handler