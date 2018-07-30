import itertools
import re
import types

#__all__ = ["RangeObject"]



class SubRange(object):
    def __init__(self, start=1, end=None, step=1):
        self._start = start
        self._end = end if end is not None else start
        if step < 1:
            raise Exception("Step needs to be greater than one")
        self._step = step
        self._sub_ranges = []

    @property
    def sub_ranges(self):
        return sorted(self._sub_ranges)
    
    def add_sub_range(self, sub_range):
        # maybe calculate new sub_ranges here
        self._sub_ranges.append(sub_range)

    @classmethod
    def from_range_str(cls, string):
        pass

    @classmethod
    def from_str_list(cls, value):
        pass
                
    def __iter__(self):
        if len(set(map(len, [x.sub_ranges for x in self.sub_ranges]))) > 1:
            raise Exception("All sub ranges must have same number of sub_ranges")
        visited = []
        for i in xrange(self._start, self._end + 1, self._step):
            if self.sub_ranges:
                for j in sorted(itertools.chain(*self.sub_ranges)):
                    result = [i] + j
                    if result not in visited:
                        visited.append(result)
                        yield result
            else:
                yield [i]

    def get_range_str(self):
        
    
    def __str__(self):
        return str(list(sorted(itertools.chain(*self.sub_ranges))))
        
    def __repr__(self):
        return '<SubRange({0})>'.format(str(self))


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
