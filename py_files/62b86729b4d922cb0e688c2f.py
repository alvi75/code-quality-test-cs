def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"key": {
			"tls": False,
			"authentication": True,
			"authorization": True,
			"etcd": True,
			"docs": True,
			"log": True,
		},
		"auth": {
			"user": user,
			"password": None,
		}
	}
	if os.environ.get("USER") is not None:
		config["key"]["authentication"] = False
	return config