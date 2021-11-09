def isSymmetricFunction(mat, N): 
    for i in range(N): 
        for j in range(N): 
            if (mat[i][j] != mat[j][i]): 
                return False
    return True
   
mat = [ [ 1, 2, 3 ], [ 2, 3, 4 ], [ 3, 4, 5 ] ] 
if (isSymmetricFunction(mat, 3)): 
    print("TRUE")
else: 
    print("FALSE")