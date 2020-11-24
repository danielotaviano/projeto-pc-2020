from getArgs import getArgs
from exceptions import raiseExceptions
from getNameFiles import getNameFiles
from getNames import getNames
from writeNames import writeNames

args = getArgs()
raiseExceptions(args)
fileName, outputNameFile = getNameFiles(args)
names = getNames(fileName)
names.sort()
writeNames(names,outputNameFile)

