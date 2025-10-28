def status_str(self, prefix=''):
	"""
	Return a string with visiting the sorted self.messages list, each visit add prefix and the element in the sorted self.messages list.
	"""
	status = ''
	for i in range(len(self.messages)):
		if i == 0:
			status += prefix + 'START\n'
		else:
			status += prefix + str(i) + '\n'
		status += self.messages[i].status_str(prefix=prefix)
	return status