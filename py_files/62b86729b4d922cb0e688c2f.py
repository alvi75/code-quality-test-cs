def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"key": {
			"tls": False,
			"authentication": None,
			"authorization": None,
			"etcd": etcd_host,
			"docs": True,
			"log": True
		},
		"auth": {
			"user": user,
			"password": None
		}
	}

	return config