
# Simple programm to create a calculator using if else 
number1 = float(input ("enter 1st number:- "))
operator= input ("operator:-  ")
number2 = float(input ("enter 2nd number:- ")) 

#Error Handling with try and Except block
try:
    # For addition operation 
   if operator== "+" :
      print ("Result: ", number1 + number2)
# For sub operation
   elif operator== "-" :
      print ("Result: ", number1 - number2)
    # For multiple operation
   elif operator== "*" :
      print ("Result: ", number1 * number2)
# For Division operation
  elif operator== "/" :
      if number2 != 0 :
         print ("Result:",number1/number2)
      elif number2 == 0:
         print ("Please Enter another Number ")
         print('Its a zero division Error')
 except:
    print ("invalid operator ")
     
