def base_config(user, etcd_host="localhost", etcd_port=2379):
		"""
		Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
		"""
		return {
			"auth": user,
			"tls": {
				"ca_cert": "/etc/ssl/certs/ca-cert.pem",
				"cert": "/etc/ssl/certs/client.crt",
				"key": "/etc/ssl/certs/client.key"
			},
			"etcd": {
				"host": etcd_host,
				"port": etcd_port
			},
			"logging": {
				"level": "info"
			}
		}