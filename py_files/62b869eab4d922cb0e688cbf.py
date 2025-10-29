def generate_default_observer_schema(app):
	"""
	Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
	"""
	for resource in app.spec.manifest:
		if not hasattr(resource, 'observers') or len(resource.observers) == 0:
			continue

		for observer in resource.observers:
			if observer['type'] != 'custom':
				continue

			if observer['name'] == 'default':
				continue

			if observer['name'] not in app.observers:
				continue

			if observer['name'] not in app.observers[observer['type']].keys():
				continue

			if observer['name'] not in app.observers[observer['type']][observer['type']]['observers']:
				app.observers[observer['type']][observer['type']]['observers'][observer['name']] = observer