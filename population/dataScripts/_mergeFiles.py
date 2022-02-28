#!/bin/python3

from sys import argv

mg = set()

for arg in argv[1:]:
    try: 
        with open(arg, "r+") as f:
            lines = f.read()

        lines = lines.splitlines()
        for ln in lines:
            mg.add(ln.strip())

    except Exception:
        raise

ls = sorted([s for s in mg])
strSet = "\n".join(ls)

with open("merged.txt", "w+") as f:
    f.write(strSet)