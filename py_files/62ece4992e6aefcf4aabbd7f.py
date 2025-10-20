def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	image_id = None
	netloc = None
	use_ssl = False

	if not image_href.startswith('http'):
		raise ValueError("Image href must start with http or https")

	parts = image_href.split('/', 1)

	if len(parts) == 2:
		image_id, netloc = parts
	else:
		raise ValueError("Invalid image href")

	if netloc in ['localhost', '127.0.0.1']:
		use_ssl = False
	elif netloc.startswith('https://'):
		use_ssl = True
		netloc = netloc[8:]
	elif netloc.startswith('http://'):
		netloc = netloc[7:]

	return image_id, netloc, use_ssl