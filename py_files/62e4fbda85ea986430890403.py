def _shuffled(seq: Sequence[str]) -> list[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	random.seed(FIXED_RANDOM_SEED)
	return random.sample(list(seq), len(seq))