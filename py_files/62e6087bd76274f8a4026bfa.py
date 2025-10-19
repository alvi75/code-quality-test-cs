def pop_u16(self):
		"""
		Remove the last two elements in self.data and return
		"""
		self._data = self._data[:-2]
		return unpack('<H', self._data)[0]