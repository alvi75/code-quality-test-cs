def round_half_to_even(n):
	"""
	Round a floating-point number
	"""
	if n >= 0:
		return int(n + 0.5) if n % 2 == 0 else int(n + 0.5) + 1
	else:
		return int(n - 0.5) if n % 2 == 0 else int(n - 0.5) - 1