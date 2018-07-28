import itertools
import re
import types

__all__ = ["RangeObject"]

class RangeNumber(object):
	def __init__(self, value=0, sub_range=None):
		self._value = value
		self._sub_range = None
	
	@property
	def sub_range(self):
		return self._sub_range

	@sub_range.setter
	def sub_range(self, sub_range):
		pass
	

class RangeObject(object):
	

	def __init__(self, values=None):
		values = values or []
		self._values = self._make_range(values)

	def __iter__(self):
		pass

	def __delitem__(self, index, stop):
		pass

	def __getitem__(self, index, stop):
		pass

	def __setitem__(self, index, stop):
		pass

	def __concat__(self, other):
		new_range = []
		pass

	def __iconcat__(self, other):
		self._range += other._range

