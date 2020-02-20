# hello world function returning string
def hello_world():
    return ('Hello, World!')

name = "Pati"


# hello name
def hello(name):
    return('Hello ' + name + "!")
    if len(name) > 0:
        hello(name)
    else:
        hello_world()


# print hello
def print_hello(name):
    print(hello(name))

print_hello(name)

# terminal: python3 homework.py
# onemore optional task

x = int(input("please write any real number "))
y = int(input("please write second real number "))

# min(x,y)
if x < 0:
    print("I said REAL NUMBER")
elif x < y:
    print("Less number is: " + str(x))
else:
    print("Less number is: " + str(y))


# max(x,y)
if x < 0:
    print("I said REAL NUMBER")
elif x > y:
    print("Greater number is: " + str(x))
else:
    print("Greater number is: " + str(y))
3

# len
iterable = len(input(str("please type any word ")))
print("Your word has " +str(iterable) + " signs")

# multiply
x = int(input("Please give first real number "))
y = int(input("Please give second real number "))

def multiply(x, y):
    if x ==0:
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

