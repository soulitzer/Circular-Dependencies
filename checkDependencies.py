import sys
import pprint
from cyclic import getCycles


def getAbsolutePath(relativePath, referencePoint):
    """Given the file's relative path, and point of reference return
    its absolute path

    """
    referencePoint = '/'.join(referencePoint.split('/')[:-1])

    while relativePath[:3] == "../":
        relativePath = relativePath[3:]
        referencePoint = '/'.join(referencePoint.split('/')[:-1])

    if relativePath[:2] == "./":
        return referencePoint + "/" + relativePath[2:]
    elif referencePoint is not "":
        return referencePoint + "/" + relativePath
    elif referencePoint == "":
        return referencePoint + relativePath


def generateGraph(totalString, ignored):
    """Creates a dependency graph given a string with the following structure:

    filename::dependencies@@file2::dependences

    Returns a dictionary with the filename as key and it's dependencies as a tuple.

    """
    dependencyGraph = {}

    fileStrings = totalString.split('@@')

    for fileString in fileStrings:
        fileParts = fileString.split('::')
        if len(fileParts) > 1:
            fileName, fileContents = fileParts
        else:
            continue

        fileName = fileName.strip()

        if fileName in ignored:
            continue

        tup = ()

        requireLines = fileContents.split('\n')
        for rl in requireLines:
            if not len(rl.split('require(\'')) > 1:
                continue

            rlParsed = (rl.split('require(\'')[1]).split('\')')[0].strip()

            if '.' not in rlParsed:
                continue

            if '/' in rlParsed:
                rlParsed = getAbsolutePath(rlParsed, fileName)

            # Add .js extension to dependency file name
            if rlParsed[-3:] is not ".js":
                rlParsed += ".js"

            tup = tup + (rlParsed,)

        dependencyGraph[fileName] = tup
    return dependencyGraph


""" Read the file containing the directory structure """
totalString = ''

try:
    f = open('output.txt', 'r')
except OSError:
    print('output.txt does not exist or could not be opened.')
    print('Exiting...')
    sys.exit()
else:
    for line in f:
        totalString += line
    f.close()


""" Files listed in ignored.txt will be ignored """
ignored = []

try:
    ignoredFile = open('ignored.txt', 'r')
except Exception:
    print('ignored.txt does not exist or could not be opened.')
else:
    for line in ignoredFile:
        ignored.append(line.strip())
    f.close()


cycles = getCycles(generateGraph(totalString, ignored))

pp = pprint.PrettyPrinter(indent=4)

for cycle in cycles:
    pp.pprint(cycle)
    print('\n')
