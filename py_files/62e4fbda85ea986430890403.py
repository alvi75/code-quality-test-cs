def _shuffled(seq: Sequence[str]) -> list[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	return list(shuffle(list(seq), random=FIXED_RANDOM_SEED))