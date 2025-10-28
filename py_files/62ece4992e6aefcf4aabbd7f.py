def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
	"""
	Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
	"""
	if not image_href.startswith('http'):
		image_href = 'http://' + image_href

	parsed_url = urlparse.urlparse(image_href)

	# If we have no scheme, then it's probably relative to the current page.
	if parsed_url.scheme == '':
		parsed_url = urlparse.urljoin(urlparse.urlparse(parsed_url.path).path,
										image_href)

	netloc = parsed_url.netloc
	use_ssl = False
	if netloc.endswith('.com') or netloc.endswith('.net') or \
			netloc.endswith('.org') or netloc.endswith('.edu'):
		use_ssl = True

	return parsed_url.hostname, netloc, use_ssl