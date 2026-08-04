def _get_resource_name_regex():
	"""
	Return the regular expressions that are used to validate the name of the Krake resources
	"""
	return {
		'network': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'subnet': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'router': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'port': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'security_group': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'security_group_rule': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'floating_ip': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'server': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'image': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'volume': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'keypair': re.compile(r'^[a-zA-Z0-9][a-zA-Z0-9\-_]{0,63}$'),
		'instance_type':