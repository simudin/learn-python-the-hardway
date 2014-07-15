from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s t %s.." %(from_file, to_file)

indata = open(from_file)
jim1 = indata.read()

print "The input file is %d bytes long."% len(jim1)

print "Does the output file exists? %r" %exists(to_file)
print "Ready, hit Return to continue, CTRL-C to abort."
raw_input("?")

out_file = open(to_file,'w')
jim = out_file.write(jim1)

print "Alrigthy, all done!"

out_file.close()
indata.close()