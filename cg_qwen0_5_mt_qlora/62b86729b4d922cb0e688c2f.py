def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"tls": False,
		"authentication": None,
		"authorization": None,
		"etcd": True,
		"docs": True,
		"log": True
	}
	return config