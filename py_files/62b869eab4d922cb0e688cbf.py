def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""

	for spec in app.spec.manifest:
		if spec.type == 'custom-resource':
			generate_custom_resource_observer_schema(spec)