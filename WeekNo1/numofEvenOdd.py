n=int(input("How many numbers will you type in? "))
even=0
odd=0
oddSum=0
for i in range(n):
    qNum=int(input())
    if qNum%2!=0:
        odd+=1
        oddSum+=qNum
    else:
        even+=1
print("Number of even numbers: "+str(even))
print("Number of odd numbers: "+str(odd))
print("Sum of odd numbers: "+str(oddSum))