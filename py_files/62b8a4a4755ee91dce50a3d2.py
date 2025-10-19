def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if not isinstance(dt, datetime.datetime):
		raise TypeError("Must provide a timezone datetime")
	return dt.replace(tzinfo=None).replace(tzinfo=self)