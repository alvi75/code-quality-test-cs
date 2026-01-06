def _extract_number_and_supplement_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	supplement = None

	if issue.find('supplement') is not None:
		supplement = issue.find('supplement').text
		number = issue.find('number').text

	return (number, supplement)