
def my_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print(f'my fruit of choice is {kwargs['fruit']}')
    else:
        print('I did not find the fruit here')


my_func(fruit='apple',veggie='cabbage')
