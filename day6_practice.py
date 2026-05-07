#creating a simple calculator
a = int(input("enter u first number: "))
b = int(input("enter u r second number: "))
op = input("enter u r operation-->+,-,*,%: ")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op== "*":
    print(a*b)
else:
    print("invalid operation")

#checking palindrome number
num = int(input("Enter a number: "))
original = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if original == rev:
    print("Palindrome")
else:
    print("Not palindrome")
#factorial of a number
n = 5
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)

#checking a number is prime or not
a = int(input("enter u r number")):
if a%1==0 and a%a==0:
    print("its a prime number"):
else:
    print("not a prime number")