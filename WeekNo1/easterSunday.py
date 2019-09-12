T=int(input("Give me a year: "))
if 1800<=T and T<=2099:
    A=T%19
    B=T%4
    C=T%7
    D=(19*A+24)%30
    E=(2*B+4*C+6*D+5)%7
    H=22+D+E
    if E==6 and D==29:
        H=50
    elif E==6 and D==28 and A>10:
        H=49
    elif H<=31:
        print("March "+str(H))
    else:
        H-=31
        print("April "+str(H))
