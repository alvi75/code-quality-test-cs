def generate_default_observer_schema(app):
		"""
		Generate the default observer schema for each Kubernetes resource present in ``spec.manifest`` for which a custom observer schema hasn't been specified.
		"""
		for k8s_resource_name, k8s_resource in app.resources.items():
			if not isinstance(k8s_resource, K8sCustomResourceDefinition):
				continue

			if 'customObserver' not in k8s_resource.metadata.labels:
				k8s_resource.metadata.labels['customObserver'] = ''

			schema_filename = os.path.join('schemas', '{}-observer.json'.format(k8s_resource_name))
			with open(schema_filename, 'w') as f:
				f.write(generate_default_observer_schema_string(k8s_resource))