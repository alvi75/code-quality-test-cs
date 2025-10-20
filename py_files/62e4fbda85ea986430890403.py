def _shuffled(seq: Sequence[str]) -> list[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	random.seed(FIXED_RANDOM_SEED)
	return [seq[i] for i in range(len(seq))]

def _shuffle(seq: Sequence[str], n: int) -> List[str]:
	"""
	Shuffle a given seq with the given FIXED_RANDOM_SEED
	"""
	if len(seq) < n:
		raise ValueError("Cannot shuffle sequence of length %d smaller than requested number of elements %d" % (len(seq), n))
	shuffled = _shuffled(seq)
	for i in range(n - 1):
		j = random.randint(0, n - 2)
		shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
	return shuffled