from sys import argv

script,infile=argv

currentFile=open(infile)

def printAll(f):
    print f.read()
    

def rewind(f):
    print "We are going to moving to the head of the file!"
    f.seek(0)

def printLine(line,f):
    print line,f.readline()

print "File name is %s" %infile
print "Print all file first: \n"
printAll(currentFile)

print "Now let't rewind"
rewind(currentFile)

currentLine=2
printLine(currentLine,currentFile)
printLine(1,currentFile)
rewind(currentFile)
printLine(currentLine,currentFile)