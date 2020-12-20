x=input('Press x to exit OR Press any other key to restart.')
while(x!='x'):
    op=int(input('\t1.Binary to Decimal \n\t2.Decimal to Binary'))
    n=int(input('Please Enter number:'))
    if (op==1):
        deci1 =int(n,2)
        print('Your answer is',deci1)
    elif(op==2):
        print('Your answer is',(bin(n))) 
    x=input('Press x to exit OR Press any other key to restart.')
