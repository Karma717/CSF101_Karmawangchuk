print("karma wangchuk")
print("Hello world")
a=2
b=3
sum=a+b
print(sum)
multi=a*b
print(multi)
print("Sum of a and b are:",sum)
print("Product of a and b are :",multi)
Name = input ("Enter your name :")
Age = input ("Enter your Age :")
print("Presenting you our HERO",Name,"Which is Living",Age,"years on EARTH!!! and eating EVERYTHING!!!")

def do_this():
    print('Doing this')

def do_that():
    print('Doing that')

match input('Do this or that?'):
    case 'this':
        do_this()
    case 'that':
        do_that()
    case _:
        print('Invalid input')
        