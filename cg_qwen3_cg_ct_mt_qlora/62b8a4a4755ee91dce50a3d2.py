def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if not isinstance(dt, datetime.datetime):
		raise TypeError("dt must be a datetime.datetime object")
	return self._to_local(dt.astimezone(self.tz))