#hello world function returning string
def hello_world():
    return ('Hello, World!')

name="Pati"

#hello name
def hello(name):
    return ('Hello ' + name +"!")
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

x=input()
y=input()

def min(x,y):
    if x<y:
        return(x)
    else:
        return(y)

min(x,y)
