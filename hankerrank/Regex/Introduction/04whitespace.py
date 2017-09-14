Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

#12 11 15 true

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())