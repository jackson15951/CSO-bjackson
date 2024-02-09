'''
hi = "Hello World!"
a = "1"
for i in range(3):
    print(hi)
    
print(type(a))

for i in range(2*5+int(a)):
    print(i*2)
    if (i == 10) == True:
        print("Umm\n",10+15)
        


time = int(input("How many minutes: "))
hours, minutes = divmod(time,60)
#print("time = %s hours and %s minutes" %(str(hours) , str(minutes)))
print("time = %i hours and %i minutes" %(hours, minutes))


'''

'''
a = input()
oper = input()
b = input()

exper = a+oper+b 
print(eval(exper))
'''
name = "name"
print("Hi %s!" %name)