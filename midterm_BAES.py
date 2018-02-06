#Mae Aubrey Baes
#github.com/aubreybaes
#maeaubrey.baes@gmail.com
#MIDTERM EXAMINATION

def match_a():
    print ("Function match_a() \n")

    aub1 = input ("Enter 1st input:")
    aub2 = input ("Enter 2nd input:")
    aub3 = input ("Enter 3rd input:")

    aub22 = []
    aub33 = []
    aub11 = []

    
    for i in aub1:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                aub11.append(i)

    for i in aub2:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                aub22.append(i)

    for i in aub3:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                aub33.append(i)

    print "1st output: ",len(aub11)
    print "2nd output: ",len(aub22)
    print "3rd output: ",len(aub33)

match_a()
print ("\n\n")






def front_x():
    print ("Function front_x()\n")

    aub1 = input ("Enter 1st input:")
    aub2 = input ("Enter 2nd input:")
    aub3 = input ("Enter 3rd input:")

    aub11 = []
    aub111 = []
    aub22 = []
    aub222 = []
    aub33 =[]
    aub333 = []

    for i in aub1:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            aub11.append(i)
        else:
            aub111.append(i) #new list of other strings
            
    print "1st output: ",sorted(aub11) + sorted(aub111) #to alphabetically arranged


    for i in aub2:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            aub22.append(i)
        else:
            aub222.append(i) #new list of other strings
            
    print "2nd output: ",sorted(aub22) + sorted(aub222) #to alphabetically arranged


    for i in aub3:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            aub33.append(i)
        else:
            aub333.append(i) #new list of other strings
            
    print "3rd output: ",sorted(aub33) + sorted(aub333) #to alphabetically arranged

    
front_x()
