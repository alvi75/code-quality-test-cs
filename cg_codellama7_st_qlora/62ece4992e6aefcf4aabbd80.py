def remove_ending_os_sep(input_list):
    """
	If input list is None, return []
    Iterate over a string list and remove trailing os seperator characters.
    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator.
    Returns:
    A list after removing trailing os seperator characters.
	"""
    if input_list is None:
        return []
    return [x[:-1] if len(x) > 1 and x[-1] == os.sep else x for x in input_list]