def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"cert": "cert.pem",
			"key": "key.pem",
			"ca": "ca.pem"
		},
		"authentication": {
			"type": "basic",
			"username": user,
			"password": "password"
		},
		"authorization": {
			"type": "basic",
			"username": user,
			"password": "password"
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"docs": {
			"path": "docs"
		},
		"log": {
			"path": "log"
		}
	}
	return config