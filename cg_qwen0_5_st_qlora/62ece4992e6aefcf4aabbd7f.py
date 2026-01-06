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
		raise ValueError("Image URL must start with http:// or https://")

	image_id = re.search(r'\/([^\/]+)$', image_href).group(1)

	if image_id is None:
		raise ValueError("No image ID found in image URL")

	image_id = image_id.replace('/', '_')

	image_id = image_id.replace(':', '_')

	image_id = image_id.replace('.', '_')

	image_id = image_id.replace('-', '_')

	image_id = image_id.replace(' ', '_')

	image_id = image_id.replace('*', '')

	image_id = image_id.replace('?', '')

	image_id = image_id.replace('#', '')

	image_id = image_id.replace('/', '_')

	image_id = image_id.replace('\\', '_')

	image_id = image_id.replace('(', '_')

	image_id = image_id.replace(')', '_')

	image_id = image_id.replace('[', '_')

	image_id = image_id.replace(']', '_')

	image_id = image_id.replace('{', '_')

	image_id = image_id.replace('}', '_')

	image_id = image_id.replace('<', '_')

	image_id = image_id.replace('>', '_')

	image_id = image_id.replace('|', '_')

	image_id = image_id.replace('!', '_')

	image_id = image_id.replace('@', '_')

	image_id = image_id.replace('%', '_')

	image_id = image_id.replace('&', '_')

	image_id = image_id.replace('$', '_')

	image_id = image_id.replace('+', '_')

	image_id = image_id.replace(',', '_')

	image_id = image_id.replace(';', '_')

	image_id = image_id.replace('=', '_')

	image_id = image_id.replace('\'', '_')

	image_id = image_id.replace('"', '_')

	image_id = image_id.replace('(', '_')

	image_id = image_id.replace(')', '_')

	image_id = image_id.replace('(', '_')

	image_id = image_id.replace(')', '_')

	image_id = image_id.replace('(', '_')

	image_id = image_id.replace(')', '_')

	image_id = image_id.replace('(', '_')

	image_id = image_id.replace('