def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if not isinstance(dt, datetime):
		raise TypeError("dt must be a datetime object")
	if not self._is_valid_tzinfo(dt.tzinfo):
		raise ValueError("dt must have a valid tzinfo attribute")

	dt = self._localize(dt)
	return self._normalize(dt.astimezone(self))