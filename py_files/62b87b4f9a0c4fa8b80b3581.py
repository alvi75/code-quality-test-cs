def scale(self, other=None, recompute=False):
	"""
	Compute or set scale (integral of the histogram).

If *other* is ``None``, return scale of this histogram.
If its scale was not computed before,
it is computed and stored for subsequent use
(unless explicitly asked to *recompute*).
Note that after changing (filling) the histogram
one must explicitly recompute the scale
if it was computed before.

If a float *other* is provided, rescale self to *other*.

Histograms with scale equal to zero can't be rescaled.
:exc:`.LenaValueError` is raised if one tries to do that.
	"""
	if other is None:
		return self._scale
	else:
		if self._scale == 0:
			raise LenaValueError('Can\'t rescale histogram with zero scale')
		if other == 0:
			self._scale = 0
			self._bin_width = 0
			self._bin_center = 0
			self._bin_edges = [0]
			self._bin_counts = []
			self._bin_sum = 0
			self._bin_sum_sq = 0
			self._bin_min = 0
			self._bin_max = 0
			self._bin_range = 0
			self._bin_count = 0
			self._bin_mean = 0
			self._bin_stddev = 0
			self._bin_variance = 0
			self._bin_skewness = 0
			self._bin_kurtosis = 0
			self._bin_entropy = 0
			self._bin_mode = 0
			self._bin_mode_count = 0
			self._bin_mode_index = 0
			self._bin_mode_bin = 0
			self._bin_mode_bin_count = 0
			self._bin_mode_bin_index = 0
			self._bin_mode_bin_edge = 0
			self._bin_mode_bin_center = 0
			self._bin_mode_bin_width = 0
			self._bin_mode_bin_min = 0
			self._bin_mode_bin_max = 0
			self._bin_mode_bin_range = 0
			self._bin_mode_bin_count = 0
			self._bin_mode_bin_mean = 0
			self._bin_mode_bin_stddev = 0
			self._bin_mode_bin_variance = 0