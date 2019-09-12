sentNc=input("Tell me your thingie: ")
reverse=len(sentNc)
rewind=""
for i in range (len(sentNc)):
    if reverse>=0:
        rewind+=sentNc[reverse-1]
        reverse-=1
print(rewind)