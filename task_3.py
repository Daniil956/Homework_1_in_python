n = int(input("Enter number: "))
index = 1
sum1 = 0
sum2 = 0

while index <= 6:
    index += 1
    m = n//10

if index == 6:
    first = n//1000
    second = n % 1000
    while first > 0:
        m = first % 10
        sum1 += m
        first = first//10
    while second>0:
        m = second%10
        sum2 += m
        second = second//10
    if sum1 == sum2:
        print("Yes")
    else:
        print("No")
else:
    print("Think again:)")