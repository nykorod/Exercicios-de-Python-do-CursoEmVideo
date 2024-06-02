c50=c20=c10=c1=0
while True: 
       n=int(input('quanto quer sacar?:  '))
       while  n >= 50:
              n-=50
              c50+=1   
       while n>=20:
              n-=20
              c20+=1
       while  n>=10:
              n-=10
              c10+=1
       while n>=1:
              n-=1
              c1+=1
       break  

print(f'''vai dar {c50} notas de 50
vai dar {c20} notas de 20
vai dar {c10} notas de 10
vai dar {c1} notas de 1''')