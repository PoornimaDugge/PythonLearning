st='Print only the words the starts with s in this sentence'

mylist=st.split()
print(mylist)

for index in mylist:
    s=index[0]
    if s[0]=='s' or s[0]=='S':
        print(index)


for x in range(0,11):
    if (x%2==0):
        print(x)


list = [x for x in range(1,51) if(x%3==0)]
print(list)

st = 'Print every word in this sentence that has an even number of letters'

st_list=st.split()

for i in st_list:
    if(len(i)%2==0):
        print(i)


st = 'Create a list of the first letters of every word in this string'

list=[x[0] for x in st.split()]
print(list)


for  num in range(1,16):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print('Fizz')
    else:
        print(num)