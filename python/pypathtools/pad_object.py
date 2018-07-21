import re


class PadObject(object):
    
    @classmethod
    def parsePadding(cls, pad_str):
        pass
    
    def __init__(self, pad_amount=1):
        self._pad_amount = pad_amount
    
    def getHashStyle(self):
        return "#" * self._pad_amount
    
    def getAtStyle(self):
        return "@" * self._pad_amount
    
    def getNukeStyle(self):
        return "$F{0}".format(self._pad_amount)
    
    def getCStyle(self):
        return "%0{0}d".format(self._pad_amount)
    
    def getRangeStyle(self, frange):
        return "{0}#".format(str(frange))
    
    def getRegexPattern(self):
        return r"(\d{{{0}}})".format(self._pad_amount)
    
    def getGlobPattern(self):
        return "[0-9]" * self._pad_amount
    
    def expand(self, frame_number):
        template = "{{0:=0{0}d}}".format(self._pad_amount)
        return template.format(frame_number)
    