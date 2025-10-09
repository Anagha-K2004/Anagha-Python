f=open("demo.txt","r")
content=f.readlines()
l=len(content)
print(l)
print(content)
for i in range(l):
    if i%2==0:
        print(content[i])
    

               
