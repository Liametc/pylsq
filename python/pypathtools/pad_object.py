import re


class PadObject(object):

	hash_regex = re.compile(r"(#+|@+)|[%\$F]+(\d+)d?")  # frame padding eg ####/@@@@/%04d/$F4

	@classmethod
	def parse_padding(cls, pad_str):
		match = cls.hash_regex.match(pad_str)
		if not match:
			return
		elif match.group(1):
			pad = len(match.group(1))  # #### or @@@@ type
		else:
			pad = int(match.group(2))  # %04d or $F4 type
		return PadObject(pad_amount=pad)
	
	def __init__(self, pad_amount=1):
		self._pad_amount = pad_amount
	
	def get_hash_style(self):
		return "#" * self._pad_amount
	
	def get_at_style(self):
		return "@" * self._pad_amount
	
	def get_nuke_style(self):
		return "$F{0}".format(self._pad_amount)
	
	def get_c_style(self):
		return "%0{0}d".format(self._pad_amount)
	
	def get_range_style(self, frange):
		return "{0}#".format(str(frange))
	
	def get_regex_pattern(self):
		return r"([-0-9]{{{0}}})".format(self._pad_amount)
	
	def get_glob_pattern(self):
		return "[-0-9]" * self._pad_amount
	
	def expand(self, frame_number):
		template = "{{0:=0{0}d}}".format(self._pad_amount)
		return template.format(frame_number)

