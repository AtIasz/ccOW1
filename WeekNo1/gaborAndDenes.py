line="<Gabor> és Denes <fel>masztak <a diofa>ra."
write=False
word=""
for i in range(len(line)):
    if line[i]=="<":
        write=True
    if line[i]==">":
        write=False
    if write==True and line[i+1]!=">":
        word+=line[i+1]
    if line[i]==">":
        print(word)
        word=""


