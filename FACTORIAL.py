print('''
hi welcome !
kindly enter a number you want to get factorial for
''')
num=input('enter a positive number:')
while not num.isnumeric():
    print('error try again')
    num=input('enter a positive number:')
while int(num)%1!=0 and int(num)<0:
    print('error enter a positive integar')
    num=input('enter a positive number:')
if int(num)==0 or int(num)==1:
    print('the factorial is 1')
else:
    fact=1
    for i in range(1,int(num)+1):
        fact*=i
        print(i,('*') )
    print('the factorial of',num,'is',fact)




