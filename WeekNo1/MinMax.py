num=int(input("How many numbers do you type? "))
min=100000000
max=0
for i in range(num):
    numNum=int(input())
    if min>numNum:
        min=numNum
    if max<numNum:
        max=numNum
print("Min: "+str(min))
print("Max: "+str(max))