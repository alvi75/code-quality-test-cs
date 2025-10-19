def hydrate_time(nanoseconds, tz=None):
		"""Convert nanoseconds to a time in fixed format."""
		if not isinstance(nanoseconds, int):
			raise TypeError("nanoseconds must be of type int")
		tz = _parse_tz(tz)
		return datetime.datetime.fromtimestamp(float(nanoseconds) / 1000000000 + tz.utcoffset(UTC).total_seconds())