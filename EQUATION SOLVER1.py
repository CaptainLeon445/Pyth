import sys
ans='y' 
while ans not in('n','N'):
    print(''' 
    WELCOME
    PRESS 1 FOR QUADRATIC EQUATION
    PRESS 2 FOR  SIMULTANEOUS EQUATION
    PRESS Q TO QUIT
    ''')
    res=input('')
    while res not in('1','2'):
        print('error!!!!!')
        res=input('enter again')
    def quad():
        a=input('enter the value of a:')
        b=input('enter the value of b:')
        c=input('enter the value of c:')
        while not a.isdecimal():
            print('error,please enter an integar')
            a=input('enter the value of a:')
        a=float(a)
        while not b.isdecimal():
            print('error,please enter an integar')
            b=input('enter the value of b:')
        b=float(b)  
        while not c.isdecimal():
            print('error,please enter an integar')
            c=input('enter the value of c:')
        c=float(c)
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
        a1=input('enter the value of a1:')
        b1=input('enter the value of b1:')
        c1=input('enter the value of c1:')
        a2=input('enter the value of a2:')
        b2=input('enter the value of b2:')
        c2=input('enter the value of c2:')
        while not a1.isdecimal():
            print('error, re-enter a a1:')
            a1=input()
        a1=float(a1)
        while not b1.isdecimal():
            print('error, re-enter value of b1:')
            b1=input()
        b1=float(b1)
        while not c1.isdecimal():
            print('error, re-enter value of c1:')
            c1=input()
        c1=float(c1)
        while not a2.isdecimal():
            print('error, re-enter value of a2:')
            a1=input()
        a2=float(a2)
        while not b2.isdecimal():
            print('error, re-enter value of b2:')
            b2=input()
        b2=float(b2)
        while not c2.isdecimal(): 
            print('error, re-enter value of c2:')
            c2=input()
        c2=float(c2)
        if ( b1*a2)-(a1*b2)==0:
            print('math error ,cant solve')
        else:
            x=((b2*c1)-(b1*c2))/((b2*a1)-(b1*a2))
            y=((c1*a2)-(c2*a1))/((a2*b1)-(a1*b2))
            print('x=',x)
            print('y=',y)
    if res=='1':
        quad()
    elif res=='2':
        simult()
    else:
        sys.exit
    print('do you want to try again,''Y'',for yes and ''N'', for no')
    ans=input('')
