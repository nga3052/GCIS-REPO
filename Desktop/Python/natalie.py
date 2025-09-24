#Natalie 413000886
A=int(input("Enter a number: "))
B=int(input("Enter a number: "))
C=int(input("Enter a number: "))
def triangle_type_checker(A,B,C):
    """this function is to define if the triangle is equilateral"""
    if A==B==C:
        return "Triangle is equilateral"
    elif A==B or B==C or C==A:
        return "Triangle is isosceles"
    else:
        return "Triangle is scalene"
    
    
print(triangle_type_checker(A,B,C))   
    
    

    

  

    
