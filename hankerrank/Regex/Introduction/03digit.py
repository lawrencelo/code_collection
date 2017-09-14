Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

# 06-11-2015 true

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())