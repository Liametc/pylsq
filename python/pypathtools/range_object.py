import itertools
import re
import types

#__all__ = ["RangeObject"]

class SubRange(object):
    def __init__(self, start=1, end=1, step=1):
        self._start = start
        self._end = end
        self._step = step
        self._sub_ranges = []

    @property
    def sub_ranges(self):
        return sorted(self._sub_ranges)
    
    def add_sub_range(self, sub_range):
        self._sub_ranges.append(sub_range)

    @classmethod
    def from_list(cls, values):
        pass
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        pass
        
    def range(self):
        for frame in xrange(self._start, self._end + 1, self._step):
            for sub_frame in itertools.chain(*self.sub_ranges):
                current = [frame]
                current.extend(sub_frame)
                yield current


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
