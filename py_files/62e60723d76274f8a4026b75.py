def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n > 0:
		return int(math.ceil(n + .5))
	else:
		return int(math.floor(n - .5))