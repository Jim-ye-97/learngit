from random import shuffle

#实现发牌操作
def dispatch(players,pCards):
    player = [None] * players
    playerCards = [player] * pCards
    cards = [None] * 52
    index=0;
    for i in range(4):
        for j in range(2,15):
            cards[index] = i * 100 + j
            index=index+1
    #洗牌
    shuffle(cards)
    #发牌
    pcIndex = 0
    for i in range(len(playerCards)):
        for j in range(len(playerCards[i])):
            playerCards[i][j]=cards[pcIndex]
            pcIndex=pcIndex+1
    return playerCards








if __name__ == "__main__":  # 当程序执行时
      players = int(input("请输入玩家个数："))
     # #print(players)
     # #判断个人
     # while (players<=2):
     #     print("请输入大于等于2的数字:")
     #     players = int(input("请输入玩家个数:"))
     # pCards = int(input("请输入每个玩家的手牌数："))
     ##判断牌张数



