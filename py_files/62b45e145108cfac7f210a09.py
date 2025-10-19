def check_digests_present_and_used(self, manifest_files, digests_used):
		"""
		Check all digests in manifest that are needed are present and used. Return error() in the class.
		"""
		for digest in digests_used:
			if not self.manifests[manifest_files[digest]['file']]['digests'].get(digest, False):
				return self.error("Digest %s is missing from manifest" % (digest,))
		return None