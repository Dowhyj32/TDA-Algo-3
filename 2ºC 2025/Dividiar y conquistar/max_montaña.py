def valor_montaña(arr, izq, der):
    
    medio = (izq+der)//2
    
    if (izq==der):
        return arr[izq]
    
    elif(arr[medio-1]>arr[medio]):
        
        return valor_montaña(arr,izq,medio-1)
    
    elif(arr[medio]<arr[medio+1]):
    
        return valor_montaña(arr,medio+1,der) 
    
    else:
        return arr[medio]
    
a = [-1,3,8,22,30,22,8,4,2,1]
a1 = [-1,3,8,22,24,26,28,10,4,2,1]
a2 = [-1,3,8,22,24,26,28,10]

res = print(valor_montaña(a,0,len(a)-1))
res1 = print(valor_montaña(a2,0,len(a2)-1))
res2 = print(valor_montaña(a2,0,len(a2)-1))