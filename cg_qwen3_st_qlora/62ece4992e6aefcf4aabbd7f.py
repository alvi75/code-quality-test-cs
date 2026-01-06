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

	if not image_href:
		raise ValueError('Image href is empty')

	if '://' in image_href:
		parts = image_href.split('://')
		if len(parts) != 2:
			raise ValueError('Invalid image href: %s' % image_href)

		image_id = parts[1]
		netloc = parts[0]

	else:
		image_id = image_href

	if netloc:
		if netloc == 'localhost':
			use_ssl = False
		elif netloc.startswith('https'):
			use_ssl = True
		else:
			use_ssl = False

	return image_id, netloc, use_ssl