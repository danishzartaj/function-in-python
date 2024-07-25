# write a function called max_of_three that takes three parameters as inputs and returns the largest of the three. The function should use conditional statements to compare the values and determine the greatest.  



def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(max_of_three(40, 30, 50))  
# //*The out put will become 50 
