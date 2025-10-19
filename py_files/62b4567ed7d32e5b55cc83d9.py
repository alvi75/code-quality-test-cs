def deep_merge_nodes(nodes):
	"""
	Merge any node values corresponding to duplicate keys and return the result. If there are colliding keys with non-MappingNode values, the last of the values remains.
	"""
	if len(nodes) == 1:
		return nodes[0]
	keys = set()
	seen_keys = {}
	result = Node()
	for n in nodes:
		if not isinstance(n, MappingNode):
			raise TypeError("Expected a list of MappingNodes")
		for k, v in iteritems_(n.value):
			if k in keys:
				if seen_keys.get(k, False):
					continue
				else:
					seen_keys[k] = True
					result.value[k].value.extend(v.value)
			else:
				keys.add(k)
				result.value[k] = deepcopy(v)
	return result