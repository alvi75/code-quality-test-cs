def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if prior.version != self.version - 1:
		self.error("Prior version is not one less than current version")
		return False
	if prior.inventory_id != self.inventory_id:
		self.error("Prior inventory ID does not match current inventory ID")
		return False
	if prior.inventory_type != self.inventory_type:
		self.error("Prior inventory type does not match current inventory type")
		return False
	if prior.inventory_type == "file":
		if prior.file_name != self.file_name:
			self.error("Prior file name does not match current file name")
			return False
		if prior.file_size != self.file_size:
			self.error("Prior file size does not match current file size")
			return False
		if prior.file_hash != self.file_hash:
			self.error("Prior file hash does not match current file hash")
			return False
		if prior.file_hash_algorithm != self.file_hash_algorithm:
			self.error("Prior file hash algorithm does not match current file hash algorithm")
			return False
		if prior.file_hash_algorithm == "sha256":
			if prior.file_hash_algorithm_version != self.file_hash_algorithm_version:
				self.error("Prior file hash algorithm version does not match current file hash algorithm version")
				return False
		if prior.file_hash_algorithm == "sha512":
			if prior.file_hash_algorithm_version != self.file_hash_algorithm_version:
				self.error("Prior file hash