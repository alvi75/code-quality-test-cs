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
			"password": "password"
		},
		"authorization": {
			"username": user,
			"password": "password"
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"docs": {
			"enabled": True
		},
		"log": {
			"level": "info",
			"file": "/var/log/etcd.log"
		}
	}

	return config