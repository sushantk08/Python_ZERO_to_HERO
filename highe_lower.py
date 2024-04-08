import random
import game_data as data

flag=True
score=0
compare1 = random.choice(data.data)
compare2 = random.choice(data.data)
while flag:
    if score>0:
        compare1=compare2
        compare2=random.choice(data.data)
    while compare1==compare2:
        compare2=random.choice(data.data)

    print(f"compare1: {compare1['name']}, a {compare1['description']}, from {compare1['country']}\n")
    print("*************** VS ***************\n")
    print(f"compare2: {compare2['name']}, a {compare2['description']}, from {compare1['country']}\n")
    result = int(input("who has more followers ? type '1' or '2': "))
    if result == 1:
        if compare1['follower_count'] > compare2['follower_count']:
            score = score + 1
            print(f"\nyou are right. your score is {score}")
        else:
            flag=False
            print(f"\nyou are wrong . . . your final score is {score}")
    elif result == 2:
        if compare1['follower_count'] < compare2['follower_count']:
            score = score + 1
            print(f"\nyou are right. your score is {score}")
        else:
            flag=False
            print(f"\nyou are wrong . . . your final score is {score}")