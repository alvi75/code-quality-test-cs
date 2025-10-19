def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n - floor(n) < 0.5:
		return floor(n)
	elif n - ceil(n) < 0.5:
		return ceil(n)
	else:
		return n if isnan(n) or isinf(n) else round_half_up(n)