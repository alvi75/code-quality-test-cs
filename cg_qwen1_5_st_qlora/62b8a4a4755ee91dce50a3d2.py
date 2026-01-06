def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if self._is_dst(dt):
		return dt.replace(tzinfo=self.tz)
	else:
		return dt.replace(tzinfo=pytz.utc).astimezone(self.tz)