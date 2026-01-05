def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n - math.floor(n) == 0.5:
		return int(math.ceil(n))
	else:
		return round(n)