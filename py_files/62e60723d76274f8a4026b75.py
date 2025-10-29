def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n - int(n) >= 0.5:
		return math.ceil(n)
	else:
		return math.floor(n)