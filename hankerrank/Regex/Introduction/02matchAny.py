regex_pattern = r'^...\....\....\....$'	# Do not delete 'r'.

import re
import sys

#123.456.abc.def true
#1123.456.abc.def false
#123.123.123.132.123.123 false

test_string = input()

match = re.match(regex_pattern, test_string) is not None
print(str(match).lower())