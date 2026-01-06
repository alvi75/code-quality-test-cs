def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if self._tzinfo is None:
		return dt

	tz = pytz.timezone(self._tzinfo)
	return tz.localize(dt)