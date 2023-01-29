n= int(input("Enter number: "))
sum = 0
while n>0:
    m = n%10
    sum += m
    n = n//10
print(sum)