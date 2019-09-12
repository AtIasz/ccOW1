mondat = input("Give me some characters: ")
metag= ""
for i in range(len(mondat)):
    if  mondat[i]!=" ":
        metag+=mondat[i]+" "
print(metag)