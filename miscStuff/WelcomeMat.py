
def printMat(_mat):
    for r in mat:
        print(''.join(r))

def insertInMiddle(a,b):
    lenB = len(b)
    lenA = len(a)
    startMid = int((lenA-lenB)/2)
    b.reverse()
    while len(b) > 0:
        a[startMid] = b.pop()
        startMid+=1
    return a

if __name__ == '__main__':
    h, w = map(int,input().split())

    mat = []
    for i in range(h):
        mat.append(list('-'*w))
    
    middle = int((h/2)-0.5) 
    # print(middle)

    mat[middle] = insertInMiddle(mat[middle],list('WELCOME'))
    # printMat(mat)

    patternCnt = 1
    for i in range(middle):
        mat[i] = insertInMiddle(mat[i],list('.|.'*(patternCnt)))
        patternCnt+=2

    patternCnt-=2
    for i in range(middle):
        mat[i+(middle+1)] = insertInMiddle(mat[i+(middle+1)],list('.|.'*(patternCnt)))
        patternCnt-=2
    
    printMat(mat)

