"""
五子棋
矩阵做棋盘  16*16  "+"
打印棋盘  for  for
游戏是否结束
开始下棋  while True  游戏是否结束：
   黑白交替   player=0  p%2==0 ==1 p+=1
   下棋动作一样 但棋子不一样
"""

board = []


# 创建棋盘
def initBroad():
    global board  # 调用全局的board
    board = [None]*16
    for i in range(len(board)):
        board[i] = ["+ "]*16


# 打印棋盘
def printBoard():
    global board
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print("")


# 开始下棋
def startGame():
    global board
    player = 0
    while isGameContinue():
        if player % 2 == 0:
            # 黑方下棋
            print("==>黑方下棋")
            if not playChess("●"):
                continue
            else:
                # 白方下棋
                print("==>白方下棋")
            if not playChess("○"):
                continue
            player += 1


def playChess(chess):
    # 获取位置
    x = int(input("==> X="))-1
    y = int(input("==> Y="))-1
    if board[x][y] == "+ ":
        board[x][y] = chess
        printBoard()
        return True  # 落子成功
    else:
        print("==> 已有棋子 请重新落子\a")
        printBoard()
        return False   # 落子失败


def isGameContinue():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "+ ":
                # 横向
                if j <= 11:
                    if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]:
                        whoWin(i, j)
                        return False
                # 竖向
                if i <= 11:
                    if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j]:
                        whoWin(i, j)
                        return False
                # 反斜
                if i <= 11 and j <= 11:
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4]:
                        whoWin(i, j)
                        return False
                # 正斜
                if i >= 4 and j <= 11:
                    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == board[i-4][j+4]:
                        whoWin(i, j)
                        return False
    return True


def whoWin(i, j):
    if board[i][j] == "●":
        print("黑方胜出")
    else:
        print("白方胜出")
    for i in range(10):
        print("\a")


initBroad()
printBoard()
startGame()
