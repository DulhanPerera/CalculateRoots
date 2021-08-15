import math  
#create variables
a = 0
b = 0
c = 0
discriminant = 0
root_1 = 0
root_2 = 0

#User Input
a=int(input("Enter the coefficient of 𝒙^2:"))
b=float(input("Enter the coefficient of 𝒙 :"))
c=float(input("Enter the constant value:"))
 
discriminant = (b**2-4*a*c)

# Output
if discriminant == 0:
    root2 = (((-b) + math.sqrt(discriminant)) / (2*a))
    root1 = (((-b) - math.sqrt(discriminant)) /(2*a))
    print("The discriminant is zero -> There are two real identical roots")
    print("The roots of x^2-",b,"x+",c,"=0","are","%0.2f"%root1,"and","%0.2f"%root2)

elif discriminant > 0:
    root2 = (((-b) + math.sqrt(discriminant)) / (2*a))
    root1 = (((-b) - math.sqrt(discriminant)) /(2*a))
    print("The discriminant is greater than zero -> There are two real distinct roots")
    print("The roots of x^2-",b,"x+",c,"=0","is","%0.2f"%root1,"and","%0.2f"%root2)

else:
    print("The discriminant is less than zero -> There are no real roots")

