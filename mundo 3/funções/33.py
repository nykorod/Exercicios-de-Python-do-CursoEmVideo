def inte(msg):
     return float(input(msg))

def area(a,b):
     return a*b
larg = inte('largura:  ')
alt= inte('altura:  ')

print(f'a area de terreno {larg}m x {alt}m é de {area(larg, alt)}m²')