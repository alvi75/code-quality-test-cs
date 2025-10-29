def dict_insert(dic, val, key, *keys):
	"""
	insert a value of a nested key into a dictionary

to insert value for a nested key, all ancestor keys should be given as
method's arguments

example:
  dict_insert({}, 'val', 'key1.key2'.split('.'))
	"""
	if len(keys) == 0:
		dic[key] = val
	else:
		if key not in dic:
			dic[key] = {}
		dict_insert(dic[key], val, *keys[1:])