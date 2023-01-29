n = int(input("Enter wibth: "))
m = int(input("Enter length: "))
k = int(input("Enter pieces: "))

if k < m*n and k%n==0 or k%m==0:
    print("Yes")
else:
    print("No")