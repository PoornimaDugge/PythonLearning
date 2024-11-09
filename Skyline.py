def myfunc(x):
    list=[]
    for i in range(len(x)):
        if i%2==0:
            list.append(x[i].lower())
        else:
            list.append(x[i].upper())
            
    return ''.join(list)
            

print(myfunc('architecture'))