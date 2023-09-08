arr=[1,2,5,6,7]
output=[]
for i in arr:
    if i%2==0:
       l=arr.index(i)
       output.insert(l,i)
    else:
        output.append(i)
print(output)


