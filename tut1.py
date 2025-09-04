#Q1
'''print("twinkle ,twinkle,little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle,twinkle,little star,\nHow I wonder what you are")'''

#Q2
'''f=input("enter first name")
l=input("enter last name")
print("name is:",f,l)
print("name written in desired order:",l,f)'''

#Q3
'''import math
r=int(input("enter radius of circle"))
area= (math.pi*(r**2))
print("area is ",area)'''

#Q4
'''L = ["Red","Green","White","Black"]
print("first element of list:",L[0])
print("last element of list:",L[-1])'''

#Q5
'''n=int(input("enter a no."))
val=n+((10*n)+n)+((100*n)+(10*n)+n)
print("required output",val)'''

#Q6
'''
string = input("Enter numbers separated by commas: ")
split = string.split(",")   # makes a list of strings

# convert strings to integers
numbers = [int(x) for x in split]

# print as list
print("List:", numbers)

# convert to tuple
print("Tuple:", tuple(numbers))
'''

#Q7
'''c=float(input("enter temperature value in celsius"))
f=((9*c)/5)+32
print("value in farenheit:",f )'''

#Q8
'''a=float(input("enter first no."))
b=float(input("enter second no."))
print("no.s before swapping: ",a,",",b)
a,b=b,a
print("no.s after swapping :",b,",",a)
print("result after adding incrementally in 1 variable: ",a+1,",",b)'''

#Q9
'''n=int(input("enter no."))
if n%2==0:
    print("It is an even no.")
else:
    print("it is odd no.")'''

#Q10
'''y=int(input("enter year "))
if (y%4==0 and y%100!=0) or (y%400==0):
    print("It is a leap year")
else:
    print("It is not a leap year")'''

#Q11
'''import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance:", distance)'''

#Q12
'''a=float(input("enter first side"))
b=float(input("enter second side "))
c=float(input("enter 3rd side"))
if a+b>=c and b+c>=a and a+c>=b:
    print("Triangle with these sides is possible")
else:
    print("Triangle with these sides cant be made")'''

#Q13
'''P=int(input("Enter the amount borrowed"))
n=int(input("enter how many times it is compunded in an year"))
t=int(input("enter for how many years has the money been borrowed"))
r=int(input("enter rate of interest"))
A=P*((1+((0.01*r)/n))**(n*t))
CI= A-P
print("the amount to be paid for the given principle amount in",t,"years is:",A)
print("the compound interest for",t,"years at the given interest rate is :",CI)'''

#Q14
'''
n = int(input("Enter a number: "))

if n < 2:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):   # check up to √n
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(n, "is prime")
    else:
        print(n, "is not prime")
'''

#Q15
'''n=int(input("enter the integer N"))
t=0
for i in range(1,n+1):
    a=i**2
    t=t+a
print(t)'''




        
   
       
       

    













