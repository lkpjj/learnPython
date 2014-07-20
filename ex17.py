from sys import argv
from os.path import exists

script,fromFile,toFile=argv

print "Copyting frome %s to %s" %(fromFile,toFile)

inFile= open(fromFile)
inData=inFile.read()

print "%s is %d bytes long"%(fromFile,len(inData))

print "Does the output file exits?\n %r"%exists(toFile)

raw_input()
outfile=open(toFile,'w')
outfile.write(inData)

print "Alright,all done"
outfile.close()
inFile.close()