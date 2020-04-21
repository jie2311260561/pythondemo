from random import random
def printInfo(): #打印提示信息
    print('这个成或许模拟比赛信息')
def getinputs():
    a = eval(input('亲输入选手A的能力值：'))
    b = eval(input('请输入选手B的能力值：'))
    c = eval(input('模拟比赛的场次'))
    return a,b,c
def simNGames(n,probA,probB):
    winA,winB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA>scoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB
def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameover(scoreA,scoreB):
        if serving == 'A':
            if random()<probA:
                scoreA+=1
            else:
                serving = "B"
        else:
            if random()< probB: 
                scoreB+=1
            else:
                serving ="A"
    return scoreA,scoreB


def gameover(A,B):
    return A == 15 or B == 15
def printSummary(winA,winB):
    n = winA + winB
    print('竞技分析开始，共模拟{}场比赛'.format(n))
    print('选手A获胜{}场比赛，占比{:0.1%}'.format(winA,winA/n))
    print('选手B获胜{}场比赛，占比{:0.1%}'.format(winB,winB/n))

def main():
    printInfo()
    probA,probB,n = getinputs()
    winA,winB = simNGames(n,probA,probB)
    printSummary(winA,winB)
main()