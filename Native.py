import math
# str=list(input("Enter a Sentence or just one word"))
# vowels=['a','e','o','i','u']
# notV=[i for i in str if i.lower() not in vowels]
# notV=''.join(notV)
# print(notV)
######################################################################
# sent=input("please enter a words")
# letter=input("plz enter a letter")
# Mylist=[]
# index=0
# for i in range(len(sent)):
#     index=sent.find(letter,index)
#     if(index != -1):
#         Mylist.append(index)
#         index=index+1
# print(Mylist)
#########################################################
#
# num=int(input("please enter a number"))
# Newlist=[]
# for i in range(1,num+1):
#     Mylist=[]
#     for x in range(1,i+1):
#         Mylist.append(i*x)
#     Newlist.append(Mylist)
#
# print(Newlist)
#
#################################################
# def TriArea(base,height):
#     return 0.5*base*height
# def rectArea(width,height=1):
#     return width*height
# def circleArea(radius):
#     return radius ** 2 * math.pi
# shape=input("Please enter t => triangle  c => circle r=>Rectangle")
# if(shape=='c'):
#     r=input("plz enter a radius")
#     print(circleArea(int(r)))
# elif(shape=='r'):
#     w=input("enter a width")
#     h=input("enter a hegiht")
#     print(rectArea(int(w),int(h)))
# elif (shape=='s'):
#     s=input("ur side length")
#     print(int(rectArea(s)))
# else:
#     w=input("enter a base")
#     h=input("enter a hegiht")
#########################################################################################
# mylist=list(input("plz enter a list of names").split(" "))
# Dict={}
# for i in mylist:
#     Dict({i[0]:i})
# print(Dict)
#############################################################################################
size=int(input("plz enter number of rows"))
for i in range(size):
    for j in range(1,size-i):
        print(" ",end="")
    for x in range(0,i+1):
        print("*",end="")
    print()
