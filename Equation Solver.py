import sys
ans='y'
while ans not in ['n','N']:
    print('''
    WELCOME
    press 1 for quadratic equation
    press 2 for simultaneous
    press Q to quit
    ''')
    res= input()
    while res not in('1','2','Q'):
        print('error!!!')
        res = input('enter again')
    def quad():
        from math import sqrt
        a=float(input('enter the value of a:'))
        b=float(input('enter the value of b:'))
        c=float(input('enter the value of c:'))
        d=(b**2)-4*a*c
        x1=(-b+(d**(0.5)))/2*a
        x2=(-b-(d**(0.5)))/2*a
        if  a!=0 and d==0:
            print('the root are equal root')
            print('the  first value of x is',x1)
            print('the  second value of x is',x2)
        elif a!=0 and d>0 :
            print('the root are real and unequal root')
            print('the  first value of x is',x1)
            print('the  second value of x is',x2)
        elif a!=0 and d<0:
            print('the root are imaginary and unequal root')
            print('the  first value of x is',x1)
            print('the  second value of x is',x2)
        else:
            print('math error')
            
    def simult():
        
        a1 = input('enter a1')
        b1 = input('enter b1')
        c1 = input('enter c1')
        a2 = input('enter a2')
        b2 = input('enter b2')
        c2 = input('enter c2')
        while not a1.isdecimal():
            print('error re-enter A1')
            a1= input()
        a1=float(a1)
        while not b1.isdecimal():
            print('error re-enter B1')
            b1= input()
        b1=float(b1)
        while not c1.isdecimal():
            print('error re-enter c1')
            c1= input()
        c1=float(c1)
        while not a2.isdecimal():
            print('error re-enter A2')
            a2= input()
        a2=float(a2)
        while not b2.isdecimal():
            print('error re-enter b2')
            b2= input()
        b2=float(b2)
        while not c2.isdecimal():
            print('error re-enter c2')
            c2= input()
        c2=float(c2)
        y= ((c1*a2)-(c2*a1))/((b1*a2)-(a1*b2))
        x=((c1*b2)-(c2*b1))/((b2*a1)-(b1*a2))
        print('x:',x)
        print('y',y)
    if res=='1':
        quad()
    elif res=='2':
        simult()
    
    else:
        sys.exit
    print('would you like to try again "y", for yes and"n",for no ')
    ans=input()


