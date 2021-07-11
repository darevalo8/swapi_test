
for x in range(101):
    linea = str(x)
    
    if x % 2 == 0:
        
        linea = linea+ " buzz"
    if x % 5 == 0:
        
        linea = linea + " bazz"
    print(linea)
