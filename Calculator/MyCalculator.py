import math

def div(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
     print('Cannot divide by zero!')   
  
def mod(x,y):
    return (x%y)  

def pow(x,y):
    return (math.pow(x,y))   

def sqrt(x):
    try:
       return (math.sqrt(x))
    except:  
        return ('Invald input! Input should be positive!')        

def sin(x):
    return (math.sin(x*(math.pi/180)))    

def cos(x):
    return (math.cos(x*(math.pi/180)))   

def tan(x):
    try:
        return (math.tan(x*(math.pi/180)))
    except:
    #print('Value undefined')
        return ('Value undefined')        

def fact(x):
    return(math.factorial(x))


