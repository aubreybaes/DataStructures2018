# EXERCISE NO. 3 - STRUCTURES
# Mae Aubrey C. Baes
# github.com/aubreybaes
# maeaubrey.baes@gmail.com
# This is a structured program combining different sequence types

aubrey = input("Enter a sentence here: ").split()
baes = [(len(aub), aub) for aub in aubrey]
print "\nEach word with its corresponding no. of letters:"
print "\t",baes
print "Sorted words according to its size:"
print "\t",sorted(baes),"\n"

print ' '.join([word for (count, word) in baes])





