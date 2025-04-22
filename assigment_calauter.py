#user input +-/*
#please enter the no 
#pleas select the opertor (+,-,/,*)
#please select the next nu
#plesse select the operatr (=)
#please selec the next number
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
num1=float(input("enter the no please"))
operator=str(input("please select the operator +-/*"))
result=num1
while(operator):
        next_result = int(input("enter another number: "))
        if(operator=='+'):
            result=num1+next_result
        elif(operator=='-'):
            result=num1-next_result
        elif(operator=='*'):
            result=num1*next_result
        elif(operator=='/'):
            result=num1/next_result
        result
        operator = input("enter the operator(+,-,*,/,=) : ")
        logging.info(f"{(result)}") 
        if(operator=='='):
             break



