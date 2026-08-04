def _parse_image_ref(image_href: str) -> Tuple[str, str, bool]:
    """
    Parse an image href into composite parts import urllib.

    :param image_href: href of an image
    :returns: a tuple of the form (image_id, netloc, use_ssl)
    :raises ValueError:
    """
    parsed_url = urllib.parse.urlparse(image_href)
    if parsed_url.scheme not in ['http', 'https']:
        raise ValueError('Invalid image href: %s' % image_href)
    return parsed_url.path.lstrip('/'), parsed_url.netloc, parsed_url.scheme == 'https'