def remove_ending_os_sep(input_list):
	"""
	If input list is None, return []
    Iterate over a string list and remove trailing os seperator characters.
    Each string is tested if its length is greater than one and if the last
    character is the pathname seperator.
    Returns:
    A list after removing trailing os seperator characters.
	"""
	if not input_list:
		return []
	for i in range(len(input_list) - 1, -1, -1):
		if input_list[i] == os.sep:
			del input_list[i]
			break
	return input_list