def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""

	for manifest in app.spec.manifest:
		if not hasattr(manifest, 'observer'):
			continue

		resource = manifest.resource
		if resource not in _DEFAULT_OBSERVER_SCHEMAS:
			continue

		schema = _DEFAULT_OBSERVER_SCHEMAS[resource]
		manifest.observer = schema