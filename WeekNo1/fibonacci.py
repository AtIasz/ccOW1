numOfFib=int(input("How many Fibonacci numbers shall I make "))
numberOne=1
numberTwo=1
print(numberOne)
print(numberTwo)
for i in range(numOfFib-2):
    eq=numberOne+numberTwo
    numberOne=numberTwo
    numberTwo=eq
    print(str(eq)+"; ")