lista=[]
for c in range(0,5):
       n=int(input('número:  '))
       if c==0 or n > lista[-1]:
              lista.append(n)
       else:
              pos=0
              while pos < len(lista):
                     if n <= lista[pos]:
                            lista.insert(pos,n)
                            break
                     pos+=1
print(f'os valores foram {lista}')
# while n.count(n[-1]) > n.count(n[-2]):
       
#        n.insert(n,0)


# for num in n:
#        print(num)
       