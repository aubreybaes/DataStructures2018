#EXERCISE NO. 5 - DICTIONARIES
#Mae Aubrey C. Baes
#github.com/aubreybaes
#maeaubrey.baes@gmail.com
#This program creates a dictionary out of dictionary


print "LET'S NOW COMPUTE YOUR FINAL GRADE!!!"

print "\tGRADING SYSTEM\n\t[enter in decimal percentage]"
Q = input("\tQuizzes: ")
E = input("\tExercises: ")
A = input("\tAttendance: ")
mae = {}
def gradecomp():
    Student = input("\nNAME:")
    
    a = input("     Enter Quizzes here: ")
    b = input("     Enter Exercises here: ")
    c = input("     Enter Attendance here: ")
    aub = {"Quiz" : list(a), "exercise": list(b),"Attendance": c,"FINAL GRADE":[]}

    aub["Quiz"] = float(sum(a)/len(a))
    aub["exercise"] = float(sum(b)/len(b))
    aub["FINAL GRADE"] = aub["Quiz"]*Q + aub["exercise"]*E + aub["Attendance"]*A
    baes = aub["FINAL GRADE"]
    print "     FINAL GRADE: ",aub["FINAL GRADE"]
    if aub["FINAL GRADE"] >= 75:
        print "     CONGRATULATIONS ",Student,",YOU'VE PASSED THE SUBJECT"
    elif aub["FINAL GRADE"] <=74:
        print "\tI'M SORRY",Student, ",YOU'VE FAILED"
    mae[Student]=baes

    x = input("\n[1] Continue... [2] Print Result     : ")
    if x == 1:
        return gradecomp()
    elif x == 2:
        print mae #it returns to a dictionary with the names as keys and the corresponding final grades as the value.


gradecomp()
