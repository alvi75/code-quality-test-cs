def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"tls": {
			"cert": "/etc/ssl/certs/cert.pem",
			"key": "/etc/ssl/certs/key.pem",
			"ca": "/etc/ssl/certs/ca.pem"
		},
		"authentication": {
			"type": "basic",
			"realm": "realm",
			"users": {
				user: "password"
			}
		},
		"authorization": {
			"type": "basic",
			"realm": "realm",
			"users": {
				user: "password"
			}
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		},
		"docs": {
			"path": "/var/www/html"
		},
		"log": {
			"path": "/var/log/etcd-api.log"
		}
	}
	return config