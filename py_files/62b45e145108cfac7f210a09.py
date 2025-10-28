def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for digest in self.digests:
		if digest not in digests_used:
			return "Error: Digest %s is required but not found" % digest

	manifest_file = None
	for file_name in manifest_files:
		if file_name.endswith(".json"):
			with open(file_name) as f:
				json_data = json.load(f)
				if 'digests' in json_data:
					manifest_file = file_name
					break

		if manifest_file is None:
			return "Error: Manifest file must be a JSON file"

	manifest_json = None
	with open(manifest_file) as f:
		manifest_json = json.load(f)

	manifest_digests = manifest_json['digests']
	manifest_digests_used = set()
		for digest in manifest_digests:
			manifest_digests_used.add(digest)

		for digest in self.digests:
			if digest not in manifest_digests_used:
				return "Error: Digest %s is required but not found" % digest

		return None