def check_digests_present_and_used(self, manifest_files, digests_used):
	"""
	Check all digests in manifest that are needed are present and used. Return error() in the class.
	"""
	for mf in manifest_files:
		digests_in_manifest = set()
		with open(mf) as f:
			for line in f.readlines():
				if not line.startswith('#') and len(line.strip()) > 0:
					digests_in_manifest.add(line.split()[1])

		digests_not_used = digests_in_manifest - digests_used

		if len(digests_not_used) > 0:
			return error("Digests {} found in {} but not used".format(sorted(digests_not_used), mf))