numOfFib=int(input("How many Fibonacci numbers shall I make "))
numberOne=1
numberTwo=1
bigNum=numberOne+numberTwo
for i in range(numOfFib-2):
    eq=numberOne+numberTwo
    bigNum+=eq
    numberOne=numberTwo
    numberTwo=eq
print(bigNum)