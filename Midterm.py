import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):

    result = 0

    if radius == 0:
        result == 0.0

    else:

        result = (math.pi) * (radius ** 2)

    return(round(result, 2))




    

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):

    result = ""

    if n < 3 or n == 3:
        result += "The triangle height should be at least 4."
    
    else:
        
        for i in range(1, n + 1):
              
            if i == 1: 
                result += "*" 
                  
            elif i == n:
                result += "*" * i

            else:

                result += "*"
            
                for j in range(i - 2): # when i == 2, j needs == 0, so the range for j has to be (1), since it is excluded, the values of j for i == 2. j = 0

                    result += (" " * j) 
                
                result += "*"
                
               
                
            result += "\n"
    
    return(result).rstrip()
print(hollow_right_triangle(4))

       
                 
              
                
              
                
    



# Q3: Inverted Pyramid
def inverted_pyramid(n):
     
    result = ""
     
    if n <= 2:
        result += "The pyramid height should be at least 3."
    
    else:
        for i in range(n):

            for k in range(i):

                result += " "
            
            for m in range(((2 * n) - 1) - ( 2 * i)):

                result += "*"
        
            result += "\n"
    
    return(result).rstrip()


            


# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()