def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not settings.USE_C_OPTIMIZATIONS:
		return False

	if os.environ.get('DJANGO_DISABLE_CACHING'):
		return False

	if django.VERSION[0] == 1 and django.VERSION[1] >= 8:
		# Django 1.8 introduced template caching, which is incompatible with our method of
		# detecting whether or not to cache a template. If this version of Django is in use,
		# disable the C optimizations.
		return False

	return True