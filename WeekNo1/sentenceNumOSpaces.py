sentNc=input("Tell me ur lie: ")
withoutSpace=""
for i in range(len(sentNc)):
    if sentNc[i]!=" ":
        withoutSpace+=sentNc[i]
print(withoutSpace)