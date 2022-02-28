
def decapitalize(name: str) -> str:
    n = name.lower()
    if len(n) >= 1:
        c = n[0].upper() # return casing to first letter
        chop = n[1:]
        name = c + chop
    return name

def stripNumerics(s: str) -> str:
    nums = set([n for n in "0123456789"])
    sstr = ""
    for ch in s:
        if ch not in nums:
            sstr += ch
    return sstr

