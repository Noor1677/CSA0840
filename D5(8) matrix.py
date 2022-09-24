def movesToChessboard(board): 
    n = len(board)
    for r in range(0, n):
        for c in range(0, n):
            if (board[0][0] and board[r][0] and board[0] and board[r] == 1):
                return -1
    rowsum = 0
    colsum = 0
    rowswap = 0
    colswap = 0
    for i in range(0, n):
        rowsum += board[i][0]
        colsum += board[0][i]
        rowswap += board[i][0] == i % 2
        colswap += board[0][i] == i % 2  
    if (rowsum != n // 2 and rowsum != (n + 1) // 2):
        return -1
    if (colsum != n // 2 and colsum != (n + 1) // 2):
        return -1
    if (n % 2):
        if (rowswap % 2):
            rowswap = n - rowswap
        if (colswap % 2):
            colswap = n - colswap
    else:
        rowswap = min(rowswap, n - rowswap)
        colswap = min(colswap, n - colswap)
    return (rowswap + colswap) // 2
if __name__  ==  "__main__":
    arr = [[0,1,1,0],
           [0,1,1,0],def shuffle(l1,l2):
    c=[]
    if len(l1)!=0 and len(l2)!=0:
      for i in range(min(len(l1), len(l2))):
        c.extend([l1[i],l2[i]])      
      c.extend(l1[i+1:] or l2[i+1:])
    else:
      c.extend(l1[0:] or l2[0:])      
    return (c)
           [1,0,0,1],
           [1,0,0,1]]
    minswap = movesToChessboard(arr)
    print("minswap is:",minswap)
