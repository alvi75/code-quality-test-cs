def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n < 0:
		n = -n
	return int(round(n + 0.5))