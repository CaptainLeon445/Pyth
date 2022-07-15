import time
res=1
dict={}
while res!='0':
    print('kindly enter your name:')
    name=input('')
    name=name.upper()
    print('''welcome''',name,' to shayo quiz app')
    delay=3
    count=delay
    for i in (delay,0,-1):
        print('the quiz starts in',count,'seconds')
        time.sleep(1)
        count=1
    print('start quiz')
    s=0
    n=10
    score=0
    while s<=n:
        time.sleep(s)
        s+=1
        if s==10:
            print('your time has over')
        print('''
        (1) evaluate 3+2-1
        (a).4
        (b).45
        (c).5
        (d).23
        ''')
        ans=input('')
        ans=ans.lower()
        if ans=='a':
            score+=20
        else:
            score+=0
        print('''
        (2) the 'o'in OAU stand for what?
        (a).obatade
        (b).owolabi
        (c).obatayo
        (d).obafemi
        ''')
        ans=input('')
        ans=ans.lower()
        if ans=='d':
            score+=20
        else:
            score+=0
        print('''
        (3) Who is the CEO of Cephas digital technology?
        (a).solomon
        (b).buhari
        (c).tayo
        (d).love johnson
        ''')
        ans=input('')
        ans=ans.lower()
        if ans=='d':
            score+=20
        else:
            score+=0
        print('''
        (4) Who is  the president of nigeria as at 2021?
        (a).president Goodluck jonathan
        (b).president muhammad Buhari
        (c).president Donald Trump
        (d).president Olusegun obasanjo
        ''')
        ans=input('')
        ans=ans.lower()
        if ans=='b':
            score+=20
        else:
            score+=0
        print('''
        (5) Who is the creator of python programming language?
        (a).Dr Smith
        (b).Dr Chen
        (c).Guido Van
        (d).Spider Man
        ''')
        ans=input('')
        ans=ans.lower()
        if ans=='c':
            score+=20
        else:
            score+=0
        print(name,''' you have successively completed the Quiz and your total score is:''',score,'%')
        dict.update({name:score})
        print('''
        you have successfully''')
        print('''
        press 1  to attempt Quiz again and 0 to exit''')
        res=input('')
    print('the score list:',dict)


    
        


