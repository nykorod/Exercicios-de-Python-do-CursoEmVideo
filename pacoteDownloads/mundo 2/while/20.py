n= int(input('termos de fibonacci:  '))
t1= 0
t2= 1
c=2
print('{} -> {} -> '.format(t1,t2), end='')
while n > c:
       t3=t1+t2
       t1=t2
       t2=t3
       c+=1
       print('{} -> '.format(t3), end='')
print('fim')
