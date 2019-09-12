numberIfOne=int(input("Give me a number "))
if numberIfOne>0:
    numberOne=int (numberIfOne)
numberIfTwo=int(input("Give me another number "))
if  numberIfTwo>0:
    numberTwo=int (numberIfTwo)
if numberOne>numberTwo:
    numberDiff=numberOne-numberTwo
else:
    numberDiff=numberTwo-numberOne
print()
print("The difference is: "+str(numberDiff))