def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n < 0:
		return -round_half_to_even(-n)
	else:
		return int(round(n))