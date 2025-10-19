def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for kind, spec in app.config.watchman.observe.items():
		if 'schema' not in spec:
			spec['schema'] = generate_observer_schema(kind)