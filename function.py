import sys
ans='y'
while ans  not in['n','N']:
    print(''' 
    WELCOME
    PRESS + FOR ADDITION
    PRESS - FOR SUBSTRACTION
    PRESS * FOR MULTIPLICATION
    PRESS / FOR DIVISION
    PRESS M FOR MODULUS
    PRESS // FOR FLOOR
    PRESS ^ FOR EXPONETIAL
    PRESS Q TO QUIT
    ''')
    res=input('')
    while res not in('+','-','*','/','M','//','^','Q'):
        print('error!!!!!')
        res=input('enter again')
    def add():
        sum=0
        a=input('enter a value or = to get result:')
        while a!='=':
            a=input('enter a value or = to get result:')
            sum+=float(a)
        print(sum)
    def sub():
        a=input('enter a value or = to get result:')
        sub=float(a)
        while a!='=':
            a=input('enter a value or = to get result:')
            if a.isnumeric():
                sub-=float(a)
            else:
                print(sub)
    def mult():
        product=1
        a=input('enter a value or = to get result:')
        while a!='=':
            a=input('enter a value or = to get result:')
            product*=float(a)
        print(product)
    def div():
        a=input('enter a value or = to get result:')
        div=float(a)
        while a!='=':
            a=input('enter a value or = to get result:')
            if a.isnumeric():
                div/=float(a)
            else:
                print(div)
    def mod():
        a=input('enter a value or = to get result:')
        mod=float(a)
        while a!='=':
            a=input('enter a value or = to get result:')
            if a.isnumeric():
                mod%=float(a)
            else:
                print(mod)
    def floor(): 
        a=input('enter a value or = to get result:')
        floor=float(a)
        while a!='=':
            a=input('enter a value or = to get result:')
            if a.isnumeric():
                floor//=float(a)
            else:
                print(floor)
    def exp():
        a=input('enter a value or = to get result:')
        exp=float(a)
        while a!='=':
            a=input('enter a value or = to get result:')
            if a.isnumeric():
                exp**=float(a)
            else:
                print(exp)
    if res=='+':
        add()
    elif res=='-':
        sub()
    elif res=='*':
        mult()
    elif res=='/':
        div()
    elif res=='//':
        floor()
    elif res=='M':
        mod()
    elif res=='^':
        exp()
    else:
        sys.exit
    print('do you want to try again,''Y'',for yes and ''N'', for no')
    ans=input('')
