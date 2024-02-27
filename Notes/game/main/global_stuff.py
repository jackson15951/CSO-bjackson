#a = 0

x = True
y = False

def thing(x): 
    global a
    a = 0
    if x:
        #global a
        a = 20

#print(a)

thing(x)

print(a)
