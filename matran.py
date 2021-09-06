import numpy as np
def ucln(aa,b):
    if aa==0: 
        return b
    if b==0:
        return aa
    if aa<0:
        aa=-aa
    if b<0:
        b=-b
    if b>aa:
        c=aa
        aa=b
        b=c
    for i in range(b,0,-1):
        if aa%i==0:
            if b%i==0:
                return i
def toigian(lst):
    uoc=lst[0]
    for i in range(1,len(lst)):
        uoc=ucln(uoc,lst[i])
    no=[]
    for i in range(len(lst)):
        no.append(int(lst[i]/uoc))
    return no
def phuDaiSo(matrix,x,y):
    phudaiso=[]
    for i in range(len(matrix)):
        if i!=x:
            lst=[]
            for j in range(len(matrix)):
                if j!=y:
                    lst.append(matrix[i][j])
            phudaiso.append(lst)

    return phudaiso

def dinhThuc(matrix):
    if len(matrix)==1: 
        return matrix[0][0]
    if len(matrix)==2: 
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    if len(matrix)==3:
        return matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+matrix[0][2]*matrix[1][0]*matrix[2][1]-matrix[0][2]*matrix[1][1]*matrix[2][0]-matrix[0][1]*matrix[1][0]*matrix[2][2]-matrix[0][0]*matrix[1][2]*matrix[2][1]
    else:
        dt=0
        for i in range(len(matrix)):
            dt+=((-1)**i)*dinhThuc(phuDaiSo(matrix,0,i))*matrix[0][i]
    '''mt=np.array(matrix)
    dt=np.linalg.det(mt)'''
    return int(dt)
def bacthang(matran):
    matrix=np.array(matran,dtype="i")
    n=len(matrix[0])
    m=len(matrix)
    for i in range(n-2):
        if matrix[i,i]==0:
            for j in range(i+1,m):
                if matrix[j,i]!=0:
                    l=matrix[i].copy()
                    matrix[i]=matrix[j].copy()
                    matrix[j]=l.copy()
                    break
        for j in range(i+1,m):
            matrix[j]=matrix[i,i]*matrix[j]-matrix[j,i]*matrix[i]
    matrix=matrix.tolist()
    for i in range(m-1,0,-1):
        if matrix[i]==matrix[i-1] or matrix[i]==[0]*n:
            del matrix[i]
        else:
            matrix[i]=toigian(matrix[i])
    matrix[0]=toigian(matrix[0])
    return matrix
def giai(matrix):
    n=len(matrix)
    matranheso=[]
    for i in range(n):
        hang=matrix[i].copy()
        hang.pop()
        matranheso.append(hang)
    D=[]
    for j in range(n):
        matrancon=[]
        for i in range(n):
            matrancon.append(matranheso[i].copy())
            matrancon[i][j]=matrix[i][n]
        D.append(dinhThuc(matrancon))
    D=toigian(D)
    return D
