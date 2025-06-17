def n_c(N, K):
    
    if K==0 or K==N:
        return 1
    
    elif K<0 or K>N:
        return 0
    
    else:
        return n_c(N-1,K-1) + n_c(N-1,K)
    
print(n_c(4,2))