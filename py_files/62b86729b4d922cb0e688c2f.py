def base_config(user, etcd_host="localhost", etcd_port=2379):
	"""
	Creates a configuration with some simple parameters, the key parameters contains "tls", "authentication", "authorization", "etcd", "docs", and "log".
	"""
	config = {
		"docs": {
			"url": "https://github.com/Robpol86/docker-py",
			"issues": "https://github.com/Robpol86/docker-py/issues"
		},
		"auth": {
			"type": user.auth_type,
			"username": user.username,
			"password": user.password,
			"token": user.token
		},
		"etcd": {
			"host": etcd_host,
			"port": etcd_port
		}
	}

	if user.tls:
		config["tls"] = {
			"ca_cert": user.ca_cert,
			"cert": user.cert,
			"key": user.key,
			"insecure": user.insecure
		}

	if user.authorization:
		config["authorization"] = {
			"type": user.authorization_type,
			"username": user.authorization_username,
			"password": user.authorization_password,
			"token": user.authorization_token
		}

	if user.log:
		config["log"] = {
			"type": user.log_type,
			"name": user.log_name,
			"level": user.log_level,
			"format": user.log_format,
			"toplevel": user.log_toplevel
		}

	return config