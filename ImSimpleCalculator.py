#Simple Calculator
#Mae Aubrey C. Baes
#github.com/aubreybaes
#maeaubrey.baes@gmail.com
#This program performs the four basic arithmetic operations


print ("WELCOME to CALCULATOR!")
def on():
        opera = input("\n\n ENTER THE OPERATION YOU WANNA USE! \n 1. ADDITION \n 2. SUBTRACTION \n 3. MULTIPLICATION \n 4. DIVISION \n 5. EXIT\n\n\n")
        if opera == 1:
                        a = input("FIRST NUMBER: ")
                        b = input("SECOND NUMBER: ")
                        sum = a + b
                        print a, "+" , b ,"=" ,sum
        elif opera == 2:
                        a = input("FIRST NUMBER: ")
                        b = input("SECOND NUMBER: ")
                        diff = a - b
                        print a, "-" , b ,"=" ,diff
        elif opera == 3:
                        a = input("FIRST NUMBER: ")
                        b = input("SECOND NUMBER: ")
                        product = a * b
                        print a, "*" , b ,"=" ,product
        elif opera == 4:
                        a = input("FIRST NUMBER: ")
                        b = input("SECOND NUMBER: ")
                        quotient = a / b
                        print a, "/" , b ,"=" ,(quotient)
        elif opera == 5:
                        print ("BYE! Thank you for using calculator.")
                        return (0)
        else:
                        print ("Invalid entry. Try again")
                        return on()
	    

        return on()

on()
