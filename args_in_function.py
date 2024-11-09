
def my_func(*args):
    return sum(args)

def my_func_1(*args):
    for value in args:
        print(value)

print(my_func(10,20,20,20,20,20,10))
my_func_1(10,1,1,1,1,1,1)