def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"ca": "/etc/ssl/certs/ca.crt",
			"cert": "/etc/ssl/certs/client.crt",
			"key": "/etc/ssl/private/client.key"
		},
		"authentication": {
			"username": user,
			"password": None
		},
		"authorization": {
			"username": user,
			"password": None
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"docs": {
			"enabled": True,
			"port": 8080
		},
		"log": {
			"level": "info",
			"file": "/var/log/etcdctl.log"
		}
	}

	return config