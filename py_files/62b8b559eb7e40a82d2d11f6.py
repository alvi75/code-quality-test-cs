def determineMetaclass(bases, explicit_mc=None):
		"""Determine metaclass from 1+ bases and optional explicit __metaclass__ """
		if not explicit_mc:
			# Use __metaclass__ if it exists.
			try: return bases[0].__metaclass__
			except AttributeError: pass

			# Try to find a metaclass in base classes.
			for base in reversed(bases): # Reverse so that we try the last one first
				mc = getattr(base, '__metaclass__', None)
				if mc is not None: break
				else: continue
			return mc

		# If no explicit mc was found, use the next best guess (if any).
		for mc in ('Type', 'Object'):
			if mc in explicit_mc: return explicit_mc[mc]
			elif mc in explicit_mc.values(): return explicit_mc[mc]

		# No explicit mc or mc values were provided; use Type or Object.
		return 'Type' if len(bases) == 1 else 'Object'

	return determineMetaclass