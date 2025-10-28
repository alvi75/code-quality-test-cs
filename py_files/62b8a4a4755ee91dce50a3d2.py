def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if self._is_dst(dt) != self._dst:
			return dt.replace(tzinfo=self)
	else:
		return dt.replace(tzinfo=None).astimezone(self)