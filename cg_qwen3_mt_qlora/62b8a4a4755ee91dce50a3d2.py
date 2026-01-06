def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if not isinstance(dt, datetime.datetime):
		raise ValueError("dt must be a datetime object")
	return self._tz.localize(dt).astimezone(self._new_tz)