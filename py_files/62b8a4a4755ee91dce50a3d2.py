def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if self._tzinfo is None:
		raise ValueError("Cannot convert from UTC to %s without specifying a timezone" % self._tzname)
	return dt.astimezone(self._tzinfo)