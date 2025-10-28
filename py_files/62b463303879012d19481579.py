def _extract_number_and_supplment_from_issue_element(issue):
	"""
	Return the possible values of number and sup from the contents of issue.
	"""
	number = None
	supplement = None

	if 'number' in issue.attrib:
		number = int(issue.attrib['number'])
	elif 'supplement' in issue.attrib:
		supplement = int(issue.attrib['supplement'])

	return (number, supplement)