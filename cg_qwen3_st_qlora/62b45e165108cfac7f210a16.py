def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if not isinstance(prior, InventoryValidator):
		raise TypeError('prior must be an instance of InventoryValidator')
	if not self.validate():
		return self.error()
	if not prior.validate():
		return prior.error()
	if self.version != prior.version:
		return self.error('Prior version does not match current version.')
	if self.inventory_id != prior.inventory_id:
		return self.error('Prior inventory ID does not match current inventory ID.')
	if self.inventory_name != prior.inventory_name:
		return self.error('Prior inventory name does not match current inventory name.')
	if self.inventory_description != prior.inventory_description:
		return self.error('Prior inventory description does not match current inventory description.')
	if self.inventory_type != prior.inventory_type:
		return self.error('Prior inventory type does not match current inventory type.')
	if self.inventory_status != prior.inventory_status:
		return self.error('Prior inventory status does not match current inventory status.')
	if self.inventory_date != prior.inventory_date:
		return self.error('Prior inventory date does not match current inventory date.')
	if self.inventory_time != prior.inventory_time:
		return self.error('Prior inventory time does not match current inventory time.')
	if self.inventory_location != prior.inventory_location:
		return self.error('Prior inventory location does not match current inventory location.')
	if self.inventory_contact != prior.inventory_contact:
		return self.error('Prior inventory contact does not match current inventory contact.')
	if self.inventory_contact_email != prior.inventory_contact_email:
		return self.error('Prior inventory contact email does not match current inventory contact email.')
	if self.inventory_contact_phone != prior.inventory_contact_phone:
		return self.error('Prior inventory contact phone does not match current inventory contact phone.')
	if self.inventory_contact_fax != prior.inventory_contact_fax:
		return self.error('Prior inventory contact fax does not match current inventory contact fax.')
	if self.inventory_contact_address != prior.inventory_contact_address:
		return self.error('Prior inventory contact address does not match current inventory contact address.')
	if self.inventory_contact_city != prior.inventory_contact_city:
		return self.error('Prior inventory contact city does not match current inventory contact city.')
	if self.inventory_contact_state != prior.inventory_contact_state:
		return self.error('Prior inventory contact state does not match current inventory contact state.')