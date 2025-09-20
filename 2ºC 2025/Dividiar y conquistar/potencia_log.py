def potencia_logaritmica(a, b):
    
    if b==0:
        return 1
    
    medio = potencia_logaritmica(a, b//2)
    
    if b%2 == 0:
        return medio * medio
    
    else:
        return a * medio * medio
    

potencia_logaritmica(3, 10)
potencia_logaritmica(2,11)
        
        
        
        
        
        