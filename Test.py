import random

#generate random matrix
def random_matrix():
    n = random.randint(1,6)
    matrix = []
    supermatrix = []
    for j in range(n):
        for i in range(n):
            matrix.append( random.randint(1,10))
        supermatrix.append(matrix)
        matrix=[]
    return supermatrix,n

#print matrix
def print_matrix(matr,n):
    for i in range(n):
        print(matr[i])
    print("\n")

#create E-matrix
def E_matrix(n):
    matrix = []
    supermatrix = []
    for j in range(n):
        for i in range(n):
            if(i==j):
                matrix.append(1)
            else:
                matrix.append(0)
        supermatrix.append(matrix)
        matrix = []
    return supermatrix


mymatrix,n = random_matrix()
E = E_matrix(n)
print("Begin:\n")
print_matrix(mymatrix,n)

#find
koef=1.
for i in range(n-1):
    #check elements
    if (mymatrix[i][i] == 0):
        index = i+1
        while(index<n-1):
            if(mymatrix[index][i+1]!=0):
                break
            else:
                index+=1
        if(mymatrix[index][i+1]==0):
            koef = 0
            print("det = 0")
            break
        else:
            for j in range(n):
                temp = mymatrix[i][j]
                mymatrix[i][j] = mymatrix[index][j]
                mymatrix[index][j] = temp
    #transform matrix
    temp = mymatrix[i][i]
    koef = koef * temp
    for j in range(n):
        mymatrix[i][j] = float(mymatrix[i][j]) / temp
        E[i][j] = float(E[i][j]) / temp
    for j in range(i + 1, n):
        temp = mymatrix[j][i]
        for k in range(n):
            mymatrix[j][k] -= mymatrix[i][k] * temp
            E[j][k] -= E[i][k] * temp
if(mymatrix[n-1][n-1]==0):
    print("det = 0")
else:
    for i in range(n-1):
        temp = mymatrix[n-i-1][n-i-1]
        koef = koef * temp
        for j in range(n):
            mymatrix[n-i-1][n-j-1] = float(mymatrix[n-i-1][n-j-1]) / temp
            E[n-i-1][n-j-1] = float(E[n-i-1][n-j-1]) / temp
        for j in range(i + 1, n):
            temp = mymatrix[n-j-1][n-i-1]
            for k in range(n):
                mymatrix[n-j-1][n-k-1] -= mymatrix[n-i-1][n-k-1] * temp
                E[n-j-1][n-k-1] -= E[n-i-1][n-1-k] * temp
    print("result:\n")
    print_matrix(E,n)