#What value does a variable receive if a function connected to the variable returns nothing?
a = 2
def returnNone(item):
    if a == 2:
        return None
    elif a == 3:
        return 4
    
check = returnNone(a)
print(check)
#################################
#Does the value None count as something?
# this = None

# if this:
#     print('This is true.')
# else:
#     print("It's not true.")
#################################
#Returning Multiple Variables
# def returnsomthing():
#     return 'this', 'that', 'otherthing'

# this1, that1, other1 = returnsomthing()
# print(that1)

#################################
#Can you change a Global Value in a function?
# a = 3

# def changeA():
#     global a
#     a = 4

# changeA()
# print(a)