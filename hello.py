# hello

def hello(name=""): #nadanie zmiennej default argument
    if len(name) > 0:
        return('Hello ' + name + "!")
    else:
        return hello_world()


print(hello())

# print hello
def print_hello(name=""): # musi byc ta defaultowa wartosc nadana gdyby nic nie bylo jako zmienna name


x = int(input("please write any real number "))
y = int(input("please write second real number "))

# min(x,y)
if x < 0:
    print("I said REAL NUMBER")
elif x < y:


if x > y:
    print("Greater number is: " + str(x))
else:
    print("Greater number is: " + str(y))


# len
iterable = len(input(str("please type any word ")))
def len(iterable):
    lenght = 0
    for i in iterable:
        lenght +=1
        return lenght

print("Your word has " +str(iterable) + " signs")

# multiply

x = int(input("Please give first real number "))
y = int(input("Please give second real number "))

def multiply(x, y):
    if x ==0:
        return 0
    elif y ==0:
        return 0
    else:
        return y + multiply(y, x-1)
print ("They multiplied gives: " + str(multiply(x,y)))

# power

def power(x ,y):
    if x == 0:
        return 0
    elif y == 0:
        return 1
    else:
        return x * power(x, y-1)
print("x powered by y gives: " + str(power(x,y)))

# def divmod(x,y):
