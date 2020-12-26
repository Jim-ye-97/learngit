from random import shuffle

#默认：玩家5名，每个玩家手上3张牌
#创造扑克牌
players = 3
pCards = 3
player = [None] * players
playerCards = [player] * pCards
cards = [None] * 52
index=0;
#i表示花色
#j表示牌值
for i in range(4):
    for j in range(2, 15):
        cards[index] = i * 100 + j
        index = index + 1
shuffle(cards)
print(cards)
#模拟发牌
player1 = [None] *3
player2 = [None] *3
player3 = [None] *3
player4 = [None] *3
player5 = [None] *3

#玩家1
for i in range(0,3):
    player1 [i] = cards[i]
#玩家2
j=0
for i in range(4,7):
    player2[j] = cards[i]
    j= j + 1
#玩家3
k=0
for i in range(8,11):
    player3[k] = cards[i]
    k = k + 1
#玩家4
l=0
for i in range(9,12):
    player4[l] = cards[i]
    l = l + 1
#玩家5
m=0
for i in range(13,16):
    player5[m] = cards[i]
    m = m + 1
#print("play1的值",player1)
#print("play2的值",player2)

#比较牌等级
def getLevel(player):
    level = 0
    if len(player)>=3:
        #print(len(player))
        #定义一个存放牌的花色的数组
        color = [None] *3
        col_len = len(color)
        #定义一个存放三张牌点数的数组
        size = [None] * 3
        siz_len = len(size)
        for i in range(col_len):
            #print("play的最初值:",player[i],"----i=",i)
            color[i]=int(player[i]/100)
        for j in range(siz_len):
            #print("play传入size的值",player[j])
            size[j]=player[j]%100
        #将三张的点数进行排序
        sorted(size)
        print("size的值",size[0],size[1],size[2])
        #判断牌的等级
        if size[0] == size[1] and size[1] == size[2]:
            level = 6
        elif color[0] == color[1] and color[1] == color[2]:
            if (size[0]+1 == size[1]) and (size[1]+1 ==size[2]):
                level = 5
            else:
                level =4
        elif (size[0]+1 == size[1]) and (size[i]+1 == size[2]):
            level = 3
        elif (size[0] == size[1] or size[1] == size[2]):
            level = 2
        else:
            level = 1
    return level

playerScores = [None] *5
playerScores[0] = getLevel(player1)
playerScores[1] = getLevel(player2)
playerScores[2] = getLevel(player3)
playerScores[3] = getLevel(player4)
playerScores[4] = getLevel(player5)

print(playerScores)

winner = int(playerScores.index(max(playerScores)))
maxScore = playerScores[winner]
#print(maxScore)
maxP = 0
for i in range(len(playerScores)):
    if playerScores[i] == maxScore:
        maxP = maxP+1
        print("赢家是第",i+1,"位玩家")
if maxP ==5:
    print("最终结果:平局")
#print("赢家是第",winner+1,"位玩家")


