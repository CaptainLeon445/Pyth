
import sys
print('welcome')
ans='y'
while ans not in('n','N'):
    print('''
 press 1 for hypotenus
 press 2 for opposite
 press 3  for adjacent 
''')
    res=input()
    while res not in('1','2','3'):
        print('error try again')
        res=input()
    def hyp():
        opp=input('enter a value of opposite:')
        adj=input(' enter a value of adjacent:')
        while not opp.isdecimal():
            print('error enter an integar ')
            opp=input('enter a value of opposite:')
        while not adj.isdecimal():
            print('error enter an integar ')
            adj=input('enter a value of adjacent:')
        opp=float(opp)
        adj=float(adj)
        hyp=((opp**2)+(adj**2))**(0.5)
        print('hypotenus=',hyp)
    def opp():
        hyp=input('enter a value of hypotenus:')
        adj=input(' enter a value of adjacent:')
        while not hyp.isdecimal():
            print('error enter an integar ')
            opp=input('enter a value of hypotenus:')
        while not adj.isdecimal():
            print('error enter an integar ')
            adj=input('enter a value of adjacent:')
        hyp=float(hyp)
        adj=float(adj)
        opp =((hyp**2)-(adj**2))**(0.5)
        print('the opposite=',opp)
    def adj():
        hyp=input('enter a value of hypotenus:')
        opp=input(' enter a value of opposite:')
        while not hyp.isdecimal():
            print('error enter an integar ')
            hyp=input('enter a value of hypotenus::')
        while not opp.isdecimal():
            print('error enter an integar ')
            opp=input('enter a value of opposite:')
        hyp=float(hyp)
        opp=float(opp)
        adj=((hyp**2)-(opp**2))**(0.5)
        print('the adjacent=',adj)
    if res=='1':
        hyp()
    elif res=='2':
        opp()
    elif res=='3':
        adj()
    else:
        sys.exit
    print('do you want to try again,''Y'',for yes and ''N'', for no')
    ans=input('')