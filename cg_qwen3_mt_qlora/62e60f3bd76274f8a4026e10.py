def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	return Structure(
		"timedelta",
		[
			Field("days", "int32"),
			Field("seconds", "int32"),
			Field("microseconds", "int32"),
		],
		value,
	)