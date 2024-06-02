# n=[]
# for c in range(0,5):
#        n.append(int(input('digite um numero:  ')))
# print(n)

a=[2,3,5,7]
# o python conecta as listas quando usar o =, oq mexer em uma, mexe na outra
# b=a

# assim, b pega apenas os valores de a
b=a[:]                    
b[2]=9                    
print(a)                  
print(b)                  
