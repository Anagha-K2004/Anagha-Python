str1=input("Enter a Sentence:")
counts=dict()
words=str1.split()
for i in words:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
print(counts)
for k,v in counts.items():
    print(k,v)
         
