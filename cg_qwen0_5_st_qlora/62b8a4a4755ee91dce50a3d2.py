def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if self._tz is None:
		raise ValueError("No timezone specified")
	return dt.astimezone(self._tz)