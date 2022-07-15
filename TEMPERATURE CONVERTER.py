print('hi welcome')
print('''
  press 1 to convert from celcius to fehrenheit
  press 2 to convert from celcius to kelvin
  press 3 to convert from kelvin to fehrenheit
  press 4 to convert from kelvin to celcuis
  press 5 to convert from fahrenheit to celcuis
  press 6 to convert from fahrenheit to kelvin
    ''')
res=input('enter here:')
while res not in('1','2','3','4','5','6'):
    print('error!,try again')
    res=input('enter here:')
if res=='1':
    print('enter the temperature in celcuis:')
    c=float(input('enter here:'))
    f=c*(9/5)+32
    print('the temperature in fehrenheit is',f,)
elif res=='2':
    print('enter the temperature in celcuis:')
    c=float(input('enter here:'))
    k=273+c
    print('the temperature in kelvin is',k)
elif res=='3':
    print('enter the temperature in kelvin:')
    k=float(input('enter here:'))
    f=(k-273)*(9/5)+32
    print('the temperature in fehrenheit is',f)
elif res=='4':
    print('enter the temperature in kelvin:')
    k=float(input('enter here:'))
    c=k-273
    print('the temperature in celcuis is',c)
elif res=='5':
    print('enter the temperature in fahrenheit:')
    f=float(input('enter here:'))
    c=(5/9)*(f-32)
    print('the temperature in celcius is',c)
else:
    print('enter the temperature in fehrenheit:')
    f=float(input('enter here:'))
    k=(5/9)*(f-32)+273
    print('the temperature in kelvin is',k)


