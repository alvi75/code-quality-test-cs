def dict_insert(dic, val, key, *keys):
	"""
	insert a value of a nested key into a dictionary

to insert value for a nested key, all ancestor keys should be given as
method's arguments

example:
  dict_insert({}, 'val', 'key1.key2'.split('.'))
	"""
	for k in keys:
		if k not in dic:
			dic[k] = {}
		dic = dic[k]
	dic[key] = val