number=int(input("Give me a number: "))
tens=0
fives=0
twos=0
ones=0
if number//10>0:
    tens=number//10
    number=number-(tens*10)
if number//5>0:
    fives=number//5
    number=number-(fives*5)
if number//2>0:
    twos=number//2
    number=number-(twos*2)
if number//1>0:
    ones=number//1
    number=number-(ones*1)
if number==0:
    print("Number of 10 value coins: "+str(tens))
    print("Number of 5 value coins: "+str(fives))
    print("Number of 2 value coins: "+str(twos))
    print("Number of 1 value coins: "+str(ones))