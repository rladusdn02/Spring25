a=int(input("Enter a digit between 0 and 999: "))
h = a//100
t = (a//10)%10
o = a%10
print("The sum of digits is", h+t+o)