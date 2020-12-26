from random import shuffle
#
# multilist1 = [[0 for col in range(5)] for row in range(3)]
# multilist2 = [0, 0, 0]
# multilist3 = [multilist2] * 5
# print(multilist3)
# cards = 52*[]
# print(len(cards))
#
# array = [0, 0, 0]
# matrix = [array] * 3
# print(matrix)
# cards =[None] * 52
# print(len(cards))
# index=0
# for i in range(4):
#     for j in range(2, 15):
#         cards[index] = i * 100 + j
#         index = index + 1
# print(cards)
# shuffle(cards)
# print(cards)
players=3
pCards=3
player = [None] * players
playerCards = [player] * pCards
cards = [None] * 52
newCards = [None] * 52
index=0;
for i in range(4):
    for j in range(2,15):
        cards[index] = i * 100 + j
        index=index+1
#洗牌
print(cards)
newCards=shuffle(cards)

#发牌
pcIndex = 0
for i in range(2):
    for j in range(3):
        print(cards[pcIndex])
        # print(pcIndex)
        playerCards [i] [j]=  cards [pcIndex]
        #print(i)
        #print(j)
        pcIndex = pcIndex + 1


print(playerCards[0][0])
print(playerCards[0][1])
print(playerCards[0][2])
print(playerCards[1][0])
print(playerCards[1][1])
print(playerCards[1][2])
print(playerCards[2][0])
print(playerCards[2][1])
print(playerCards[2][2])
