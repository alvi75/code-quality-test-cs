def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n < 0:
		return -round(-n, 1)
	else:
		return round(n, 1)