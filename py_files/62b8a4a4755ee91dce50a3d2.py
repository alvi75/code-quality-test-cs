def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if not isinstance(dt, datetime):
		raise TypeError("dt must be a datetime object")
	if self._is_aware(dt):
		dt = self._localize(dt)
	return self._normalize(dt.astimezone(self))