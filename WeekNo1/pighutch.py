width=8  #int(input("Give me the width of the hutch: "))
height=4 #int(input("Give me the height of the hutch: "))
for i in range(height):
        if i==0 or i==(height-1):
            print("*"*width)
        else:
            print("*"+" "*(width-2)+"*")
            