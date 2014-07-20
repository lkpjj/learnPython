from sys import argv

script,filename = argv

print "you are running %s script,and filename is %s" %(script,filename)

print "we will read %s ..."%filename
source=open(filename)

print "input the filename you want to save"
savefile=raw_input(">")
print "writing %s ..."%savefile

target=open(savefile,'w')
target.write(source.read())
target.close()