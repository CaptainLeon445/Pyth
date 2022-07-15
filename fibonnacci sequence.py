nterms=int(input('enter the number of terms'))
n1,n2=0,1
count=0
while nterms<=0:
    print('please enter positive number')
    nterms=int(input('enter the number of terms'))
if nterms ==1:
    print('the fibonnaci sequence upto',nterms,'terms is',nterms)
else:
    print('fibonnaci sequence')
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    
    
    


