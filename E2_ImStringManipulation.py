# EXERCISE NO. 2 -  STRING MANIPULATION
# Mae Aubrey C. Baes
# github.com/aubreybaes
# maeaubrey.baes@gmail.com

a = input("\nEnter words here: ")
print ("\n1. ACCESS CHARACTER \t6. REPLACE \n2. FIND \t\t\t    7. REVERSE \n3. GET THE SIZE \t    8. UPPERCASE ALL \n4. COUNT THE SPACES  \t9. LOWERCASE ALL\n5. SPLIT ")

def string():
    x = input("\nChoose an action: ")
    if x == 1:
        b = input("\tEnter an index: ")
        print "\tThe character in index",b,"is \"",a[b],"\""

    elif x == 2:
        b = input("\tEnter a character: ")
        print "\t",b, "is in index ",a.find(b)

    elif x == 3:
        print "\tThe length is ",len(a)

    elif x == 4:
        print "\tThe number of spaces is",a.count(" ")

    elif x == 5:
        print "\t",a.split(' ')

    elif x == 6:
        y =  input("\tEnter the character or word you want to replace:")
        z = input("\tReplace it by: ")
        print "\t",a.replace(y,z)

    elif x == 7:
        list(a)
        print "\t",a[::-1]

    elif x == 8:
        print "\t",a.upper()

    elif x == 9:
        print "\t",a.lower()
    return string()

string ()
