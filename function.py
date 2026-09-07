# def sum(a,b):
#     print(a+b)
# sum(5,6)
# def sub(a,b):
#     print(a-b)
#     sum(10,5)
# sub(10,5)

# def div(a,b):
#     print(a/b)
#     return a,b
# d=div(2,4)
# print(d)

# def mod(a,b):
#     print(a%b)
#     return a,b
# mod(10,2)
# mod(5,3)

# def dd(a,b):
#     print(a//b)
#     return a,b
# dd(10,6)

# def sq(a):
#     print(a**a)

# sq(2)


# def ari(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
# ari(1,2)

# def name(a):
#     print(a)
# name("rinsy")

# def name(a):
#     print("my name  is",a)
# name("rinsy")



# # ----------types of parameter
# # 1-------multiple parameter and arguments
 
# def new(a,b):
#     print(a+b)

# new(3,5)

# # 2------------defualt parameter value

# def greet(name,message="welcome"):# welcome is defualt value
#     print(message,name)

# greet("john")
# greet("manu","thank you")
# greet("hi","anu")

# def inva(name="rinu",msg=0):
#     print(name,msg)

# inva("anu","whatsup")

# 3-------------keyword argument
def keyword(name,place):
    print(name,place)

keyword(name="rahul",place="mlp")
keyword(place="mlp",name="rahul")

# 4--------positional argument
# def new(a,b):
#     print(a,b)

# new(3,5)

# def list(name,age):
#     print(name,age)

# list("jojo",33)

# arbitary argument
# def sum(*argument)
def show(*args):
    print(args)

show(10, 20, 30, 40)

# arbitary  keyword argument
# def sum(**kwargs)
def student(**kwargs):
    print(kwargs)

student(name="Rinshila", age=16, course="Python",mark=99)
