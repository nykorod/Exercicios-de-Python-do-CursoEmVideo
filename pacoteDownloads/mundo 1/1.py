import math

n1=float(input('digite um numero '))
seno = math.sin(math.radians(n1))
cos = math.cos(math.radians(n1))
tan = math.tan(math.radians(n1))

print('o seno, cosseno e tangente de {} são {:.2f}, {:.2f} e {:.2f}'.format(n1, seno, cos, tan))
