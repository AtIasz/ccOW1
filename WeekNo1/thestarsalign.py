number=int (input("Star line's number: "))
growin=1
for i in range(number):
    print(" "*(number-i)+"*"*growin)
    growin+=2