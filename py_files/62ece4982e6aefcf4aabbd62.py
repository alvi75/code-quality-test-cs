def _replace_url_args(url, url_args):
    """
    Replace the value in url with the value in url_args
    If url_args has a value, iterate over the keys and values from url_args.
    Then replace the keys of the first parameter with values.
    Returns: the modified url.
    """
    for key, val in url_args.items():
        if key in url:
            url = url.replace(key, val)
    return url