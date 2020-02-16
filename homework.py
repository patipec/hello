#hello world function returning string
def hello_world():
    return ('Hello, World!')


name ="Pati"

#hello name
def hello(name):
    return('Hello ' + name +"!")
    if len(name)>0:
        hello(name)
    else:
        hello_world()


#print hello
def print_hello(name):
    print(hello(name))

print_hello(name)

#terminal: python3 homework.py
#onemore optional task

#zapytać Piotra czy input to jest ta zakazana built-in function?
x= int(input("please write any real number"))
y= int(input("please write second real number"))

#min(x,y)
if x<y:
    print(x)
else:
    print(y)


#max(x,y)
if x>y:
    print(x)
else:
    print(y)


#len
iterable=len(input("please type any word"))

print(iterable)