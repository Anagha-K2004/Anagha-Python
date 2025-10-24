#co2_8Accept a list of words and return the length of the longest word
l=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    word=input("Enter the word:")
    l.append(word)
print(l)
le=0    
for i in l:
    if len(i)>le:
        le=len(i)
        longword=i
print("Length of the longest word is:",le,longword)
