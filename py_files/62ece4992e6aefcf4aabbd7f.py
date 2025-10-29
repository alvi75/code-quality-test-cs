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
		raise ValueError("Image URL must start with http")

	image_href = image_href[4:]

	if image_href.endswith('/'):
		image_href = image_href[:-1]

	if image_href.startswith('//'):
		image_href = 'https' + image_href[2:]

	if image_href.startswith('https://'):
		use_ssl = True
	elif image_href.startswith('http://'):
		use_ssl = False
	else:
		raise ValueError("Invalid image URL")

	try:
		image_id = re.search(r'\d+', image_href).group(0)
	except AttributeError:
		raise ValueError("Invalid image URL")

	try:
		netloc = urllib.parse.urlparse(image_href)[0]
	except Exception:
		raise ValueError("Invalid image URL")

	return image_id, netloc, use_ssl