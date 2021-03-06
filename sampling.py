import sys
import random

targetSampling = 100000
inputFile = '/data1/nsrg/kwang40/2019-01-17-urls.txt'
outputFile = sys.argv[1]

with open(inputFile) as f:
    domainSet = f.readlines()

ratio = len(domainSet) / targetSampling / 2

outputSize = 0
with open (outputFile, 'w') as f:
    for i in range(len(domainSet)):
        if random.randint(1,ratio) == 1:
            f.write(domainSet[i])
            outputSize += 1
            if outputSize == targetSampling:
                break
