def main(x, y):
    estado, camino = convertibilidad(x, y)
    if estado:
        print('YES')
        print(len(camino))
        print(*camino)
    else:
        print('NO')
    
def convertibilidad(x, y):
    camino = [y]
    while y>x:
        if y%2==0:
            y = y//2
        elif y%10==1:
            y = y//10
        else:
            return False, []
        camino.append(y)
    
    if y==x:
        camino.reverse()
        return True, camino
    
    return False, []
    
        
ejemplos = [[1,82],[2,45]]

for i in range(len(ejemplos)):
    main(ejemplos[i][0],ejemplos[i][1])