def randomize(seq):
		""" Shuffle a sequence """
		random.seed(FIXED_RANDOM_SEED)
		rand = random.Random()
		for i in range(len(seq)):
			rand.shuffle(seq, key=lambda x: x[i])
		return seq

	return randomize