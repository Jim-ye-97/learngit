#炸金花


#生成52张牌
def create_pooks():
    pook_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
    pook_flowers = ['♥', '♠', '♣', '♦']
    pooks = []
    for pook_flower in pook_flowers:
        for pook_number in pook_numbers:
            pooks.append([pook_flower + pook_number])
    print(pooks)

create_pooks()



