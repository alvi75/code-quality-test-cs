def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {}
	config['tls'] = {
		'enabled': True,
		'certfile': os.path.join(os.path.dirname(__file__), 'ca.crt'),
		'skip_ca_cert': False,
	}
	config['authentication'] = {
		'username': user,
		'password': None,
	}
	config['authorization'] = {
		'allow_all': False,
		'allow_any': False,
		'allow_any_user': False,
		'allow_any_group': False,
		'allow_any_role': False,
		'allow_any_service': False,
		'allow_any_user_group': False,
		'allow_any_user_role': False,
		'allow_any_service_group': False,
		'allow_any_service_role': False,
		'allow_any_user_group_role': False,
		'allow_any_service_group_role': False,
		'allow_any_service_user_group_role': False,
		'allow_any_user_group_service_role': False,
		'allow_any_service_user_role': False,
		'allow_any_service_group_service_role': False,
		'allow_any_user_service_role': False,
		'allow_any_service_user_group_service_role': False,
		'allow_any_user_service_group_service_role': False,
		'allow_any_user_service_user_group_service_role': False,
		'allow_any_user_service_user_role': False,
		'allow_any_user_service_group_role': False,
		'allow_any_user_service_group_service_role': False,
		'allow_any_user_service_user_role': False,
		'allow_any_user_service_user_group_role': False,
		'allow_any_user_service_service_role': False,
		'allow_any_user_service_user_group_service_role': False,
		'allow_any_user_service_service_user_role': False,
		'allow_any_user_service_service_user_group_role': False,
		'allow_any_user_service_service_user_role': False,
		'allow_any_user_service_service_user_group_role': False,
		'allow_any_user_service_service_user_role': False,
		'allow_any_user_service_service_user_group_role': False