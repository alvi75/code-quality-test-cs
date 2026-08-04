def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		'cluster': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'node': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'network': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'subnet': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'security_group': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'security_group_rule': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'volume': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'snapshot': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'image': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'instance': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'instance_type': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'instance_type_size': r'^[a-z0-9]([-a-z0-9]*[a-z0-9])?$',
		'instance_type_size_disk': r'^[a-z0-9]([-a-