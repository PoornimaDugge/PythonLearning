
mylist= [num for num in range(0,11) if num%2==0]
print(mylist)

results= [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

results1 =[]

for x in [2,4,6]:
    for y in [1,10,100]:
        results1.append(x*y)

print(results1)

results3 =[x*y for x in [2,4,6] for y in [1,10,100]]


print(results3)