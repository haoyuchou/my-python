board=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3==0 and i!=0:
            print('-------------')
        for j in range(len(bo[0])):
            if j % 3==0 and j!=0:
                    print('|',end='')
            if j==8:
                    print(bo[i][j])
            else:
                    print(str(bo[i][j])+'',end='')


def findempty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i,j) #row col
    return None        

def valid(bo,num,po):
    for i in range(len(bo[0])): #row
        if bo[po[0]][i]==num and po[1] !=i:
            return False
    for i in range(len(bo)):#col
        if bo[i][po[1]]==num and po[0] !=i:
            return False

    boxx=po[0]//3
    boxy=po[1]//3
    for i in range(boxx*3,boxx*3+3):
        for j in range(boxy*3,boxy*3+3):
            if bo[i][j]==num and (i,j)!=po:
                return False
    return True
def solve(bo):
    find=findempty(bo)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col]=0
    return False
print_board(board)
solve(board)
print()
print_board(board)
                 


    

        
