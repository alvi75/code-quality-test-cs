def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for resource in app.config['manifest']['resources']:
		if 'observer' not in resource:
			resource['observer'] = {
				'schema': {
					'$schema': 'http://json-schema.org/draft-04/schema#',
					'title': 'Observer Schema',
					'description': 'Schema for the observer of this resource.',
					'type': 'object',
					'properties': {
						'enabled': {
							'type': 'boolean',
							'description': 'Whether or not to enable the observer.'
						},
						'interval': {
							'type': 'integer',
							'description': 'The interval at which to check the resource for changes.'
						}
					},
					'required': [
						'enabled'
					]
				}
			}