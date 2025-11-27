#co1_3 list comprehension.Generate posititve list of numbers from a given list of integers
#n=[-5,3,0,8,-2,7,-1]
#pn=[i for i in n if i > 0]
#print(pn)

#Square of N numbers.
#n=int(input("Enter the limit:"))
#s=[i*i for i in range(1,n+1)]
#print(s)

#form a list of vowels from a given word
word=input("Enter the Word:")
vow=[i for i in word if i.lower()in ("aeiou")]
print(vow)
