#!/bin/python3

from modules import *

js = jsonFromFile("seattle.json") #9MB, not going in the repo

namesLs = []
for rw in js["data"]:
    namesLs.append(rw[10])

na = NamesAggregator(namesLs)

na.dedupeNames()
na.filterOutCommonNames()
na.splitMultisFromList()

na.writeOutNameList(na.names, "seattleNames")
na.writeOutNameList(na.multinames, "seattleMultiNames")