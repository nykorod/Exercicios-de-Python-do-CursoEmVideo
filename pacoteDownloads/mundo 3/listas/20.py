lin1=[[], [], []]
lin2=[[], [], []]
lin3=[[], [], []]
for c in range(0,9):
       n=int(input('numero:  '))
       if c < 3:
              lin1[c].append(n)
       if c < 6:
              lin2[c-3].append(n)
       else:
              lin3[c-6].append(n)
print(lin1)
print(lin2)
print(lin3)