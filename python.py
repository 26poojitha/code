'''from datetime import *
d=date.today()
print(d)
d=date(2004,6,26)
for x in range(1,10):
    nextdate = d + timedelta(days=x)
    print(nextdate)'''

import sys
if len(sys.argv)<2:
    print("Usage: python hi.py <name>")
else:
    name = sys.argv[1]
    print(f"Student , {name}!")