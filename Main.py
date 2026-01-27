number1 = float(input ("enter 1st number:- "))
operator= input ("operator:-  ")
number2 = float(input ("enter 2nd number:- "))

if operator== "+" :
    print ("Result: ", number1 + number2)

elif operator== "-" :
    print ("Result: ", number1 - number2)
    
elif operator== "*" :
    print ("Result: ", number1 * number2)

elif operator== "/" :
    if number2 != 0 :
        print ("Result:",number1/number2)
        if number2 == 0: 
            print ("error!")
            
        
            
else :
    print ("invalid operator ")
