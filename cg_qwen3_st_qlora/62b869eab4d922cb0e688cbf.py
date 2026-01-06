def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""

	for resource in app.spec.manifest:
		if not app.spec.manifest[resource].get('observer'):
			app.spec.manifest[resource]['observer'] = {
				'kind': 'default',
				'schema': {
					'properties': {}
				}
			}