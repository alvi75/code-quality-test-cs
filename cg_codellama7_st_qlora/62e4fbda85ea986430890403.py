def _shuffled(seq: Sequence[str]) -> list[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	random.Random(FIXED_RANDOM_SEED).shuffle(seq)
	return seq