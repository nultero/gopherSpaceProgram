import json

validChars = set([c for c in "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"])

# get raw json to find & rip out the name fields
def jsonFromFile(fileName: str) -> dict:
    try:
        with open(fileName, "r+") as f:
            return json.loads(f.read())

    except Exception:
        raise

# used to run functions in stages over a list of names
class NamesAggregator():
    def __init__(self, names: list[str]) -> None:
        self.names = names
        self.multinames = []

    def dedupeNames(self):
        nameSet = set()
        names = self.names
        self.names = []

        while len(names) > 0:
            n = names[0]
            names = names[1:]
            if n is None:
                continue # elide an empty entry
            nameSet.add(n)

        for n in nameSet:
            self.names.append(n)

    def splitMultisFromList(self):
        names = self.names
        self.names = []
        for n in names:
            if " " in n:
                self.multinames.append(n)
            else:
                self.names.append(n)

    def filterOutCommonNames(self): # these are boring and I don't want them
        commons = set()
        with open("_mostCommonNames.txt", "r") as f:
            lst = f.readlines()
            for ln in lst:
                commons.add(ln)

        newLs = []
        for name in self.names:
            if name not in commons:
                newLs.append(name)

        self.names = newLs

    def listToLines(self, ls: list[str]) -> str:
        return "\n".join(sorted(ls))

    def writeOutNameList(self, ls: list[str], outfile: str):
        names = self.listToLines(ls)
        with open(f"{outfile}.txt", "w+") as f:
            f.write(names)

        print(f"written out {len(ls)} lines to {outfile}")

