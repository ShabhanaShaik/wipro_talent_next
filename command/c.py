import sys
if len(sys.argv)<2:
    print("Usage:python hi.py <name>")
else:
    name=sys.argv[2]
    print(f"student,{name}!")